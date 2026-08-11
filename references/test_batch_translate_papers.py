from __future__ import annotations

import unittest

import batch_translate_papers as batch


class IdentityTranslator:
    def translate(self, text: str) -> str:
        return text


class CaptionParsingTests(unittest.TestCase):
    def test_period_delimited_caption_is_detected(self) -> None:
        self.assertIsNotNone(batch.CAPTION_RE.match("Figure 1. Lumbar posture"))

    def test_fig_abbreviation_with_period_is_detected(self) -> None:
        self.assertIsNotNone(batch.CAPTION_RE.match("Fig. 2. Results"))

    def test_parenthesized_in_text_reference_is_not_caption(self) -> None:
        self.assertIsNone(batch.CAPTION_RE.match("Figure 3) shows the result"))

    def test_standalone_table_caption_is_merged(self) -> None:
        lines = ["Table 1", "Mean sagittal spinal angles", "Header"]

        merged = batch.merge_caption_lines(lines)

        self.assertEqual(merged[0], "Table 1. Mean sagittal spinal angles")
        self.assertEqual(merged[1], "Header")


class DocumentParsingTests(unittest.TestCase):
    def test_page_markers_and_numbered_references_are_preserved(self) -> None:
        source = """===== PAGE 1 =====
ABSTRACT
Summary text.
REFERENCES
1. First reference.
2. Second reference.
"""

        document = batch.parse_document(source, "Fallback")

        self.assertIn("<!-- Page 1 -->", document.paragraphs)
        self.assertIn("__REF__ 1. First reference.", document.paragraphs)
        self.assertIn("__REF__ 2. Second reference.", document.paragraphs)

    def test_table_inside_references_does_not_corrupt_reference_item(self) -> None:
        source = """References
Andersson, B.J., Ortengren, R., Nachemson, A.L., Elfstrom, G., Broman, H., 1975. First reference.
Astfalck, R.G., O'Sullivan, P.B., Straker, L.M., Smith, A.J., Burnett, A., Caneiro, J.P., Dankaerts, W., 2010. Sitting postures and trunk muscle activity in adolescents
Table 2
Coronal angle data in the three posture conditions.
===== PAGE 7 =====
with and without nonspecific chronic low back pain.
Battie, M.C., Videman, T., Gibbons, L.E., Fisher, L.D., Manninen, H., Gill, K., 1995. Third reference.
"""

        document = batch.parse_document(source, "Fallback")

        self.assertIn(
            "__REF__ Astfalck, R.G., O'Sullivan, P.B., Straker, L.M., Smith, A.J., Burnett, A., Caneiro, J.P., Dankaerts, W., 2010. Sitting postures and trunk muscle activity in adolescents with and without nonspecific chronic low back pain.",
            document.paragraphs,
        )
        self.assertIn("Table 2. Coronal angle data in the three posture conditions.", document.paragraphs)
        self.assertIn("<!-- Page 7 -->", document.paragraphs)

    def test_author_list_before_year_is_treated_as_same_reference(self) -> None:
        source = """References
Andersson, B.J., Ortengren, R., Nachemson, A.L., Elfstrom, G., Broman, H., 1975. First reference.
Astfalck, R.G., O'Sullivan, P.B., Straker, L.M., Smith, A.J., Burnett, A., Caneiro, J.P.,
Dankaerts, W., 2010. Second reference.
Battie, M.C., Videman, T., Gibbons, L.E., Fisher, L.D., Manninen, H., Gill, K., 1995. Third reference.
"""

        document = batch.parse_document(source, "Fallback")

        self.assertIn(
            "__REF__ Astfalck, R.G., O'Sullivan, P.B., Straker, L.M., Smith, A.J., Burnett, A., Caneiro, J.P., Dankaerts, W., 2010. Second reference.",
            document.paragraphs,
        )


class MarkdownRendererTests(unittest.TestCase):
    def setUp(self) -> None:
        self.renderer = batch.MarkdownRenderer(IdentityTranslator())

    def test_simple_table_is_rendered_without_flattened_duplicate(self) -> None:
        source = """Table 1. Participant characteristics
All (n = 2) Male (n = 1)
Age, years 35.5 ± 2.0 36.0 ± 1.0
BMI 20.0 ± 1.0 21.0 ± 2.0
2.3. Experimental Set-Up
Following section text.
"""

        document = batch.parse_document(source, "Test paper")
        output = self.renderer.render(document)
        table = document.simple_tables["Table 1"]

        self.assertEqual(table.headers, ["All (n = 2)", "Male (n = 1)"])
        self.assertIn("| 변수 | All (n = 2) | Male (n = 1) |", output)
        self.assertNotIn("Age, years 35.5", output)
        self.assertIn("### 2.3. Experimental Set-Up", output)

    def test_generated_output_is_marked_for_review(self) -> None:
        source = """Abstract
Summary text.
"""

        document = batch.parse_document(source, "Test paper")
        output = self.renderer.render(document)

        self.assertIn(batch.GENERATED_STATUS, output)
        self.assertIn(batch.REVIEW_REQUIRED_STATUS, output)
        self.assertLess(
            output.index(batch.GENERATED_STATUS),
            output.index("## 논문 정보"),
        )

    def test_unverified_table_is_marked_for_review(self) -> None:
        source = """Table 2. Complex outcomes
Condition A Condition B
Mixed qualitative values
3. Results
Result text.
"""

        document = batch.parse_document(source, "Test paper")
        output = self.renderer.render(document)

        self.assertNotIn("Table 2", document.simple_tables)
        self.assertIn("<!-- REVIEW REQUIRED: Table 2 -->", output)
        self.assertIn("## 3. Results", output)


if __name__ == "__main__":
    unittest.main()