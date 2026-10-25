# 합성 표면근전도 원자료를 분석하고 네 개의 설명용 그림을 생성한다.
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.integrate import cumulative_trapezoid
from scipy.signal import butter, sosfiltfilt

SCRIPT_DIRECTORY = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIRECTORY / "multifidus_resting_surface_emg_1000Hz_1s_raw.json"
OUTPUT_DIRECTORY = SCRIPT_DIRECTORY / "emg_plot_output"

LOW_CUTOFF_HZ = 20.0
HIGH_CUTOFF_HZ = 450.0
FILTER_ORDER = 4
RMS_WINDOW_SECONDS = 0.5
FIGURE_SIZE_INCHES = 2 / 2.54
PLOT_DPI = 600
TITLE_FONT_SIZE = 11
LABEL_FONT_SIZE = 10
ANNOTATION_FONT_SIZE = 10


def load_emg_data(input_path: Path) -> tuple[pd.DataFrame, int]:
    """Read the synthetic EMG JSON and return a time-indexed data frame."""
    with input_path.open(encoding="utf-8") as source:
        payload = json.load(source)

    metadata = payload["metadata"]
    sampling_rate_hz = metadata["sampling_rate_hz"]
    data_frame = pd.DataFrame(payload["samples"])

    required_columns = {"index", "time_s", "emg_mV"}
    missing_columns = required_columns.difference(data_frame.columns)
    if missing_columns:
        raise ValueError(f"Missing JSON sample fields: {sorted(missing_columns)}")
    if len(data_frame) != metadata["sample_count"]:
        raise ValueError("Metadata sample_count does not match the number of samples.")
    if not np.allclose(np.diff(data_frame["time_s"]), 1 / sampling_rate_hz):
        raise ValueError("Sample time intervals do not match sampling_rate_hz.")

    return data_frame, sampling_rate_hz


def bandpass_filter(signal_mV: np.ndarray, sampling_rate_hz: int) -> np.ndarray:
    """Apply the 20-450 Hz fourth-order Butterworth band-pass filter in introduce.md."""
    sos = butter(
        FILTER_ORDER,
        [LOW_CUTOFF_HZ, HIGH_CUTOFF_HZ],
        btype="bandpass",
        fs=sampling_rate_hz,
        output="sos",
    )
    return sosfiltfilt(sos, signal_mV)


def calculate_rms(filtered_signal_mV: np.ndarray, sampling_rate_hz: int) -> pd.DataFrame:
    """Calculate non-overlapping 0.5-second RMS values."""
    samples_per_window = int(RMS_WINDOW_SECONDS * sampling_rate_hz)
    if len(filtered_signal_mV) % samples_per_window != 0:
        raise ValueError("The signal length must be divisible by the RMS window length.")

    rms_values = []
    for start_index in range(0, len(filtered_signal_mV), samples_per_window):
        window = filtered_signal_mV[start_index : start_index + samples_per_window]
        rms_values.append(
            {
                "window_start_s": start_index / sampling_rate_hz,
                "window_end_s": (start_index + samples_per_window) / sampling_rate_hz,
                "rms_mV": np.sqrt(np.mean(np.square(window))),
            }
        )
    return pd.DataFrame(rms_values)


def calculate_mdf(filtered_signal_mV: np.ndarray, sampling_rate_hz: int) -> tuple[np.ndarray, np.ndarray, float]:
    """Calculate a one-second FFT power spectrum and its median frequency."""
    frequencies_hz = np.fft.rfftfreq(len(filtered_signal_mV), d=1 / sampling_rate_hz)
    fft_values = np.fft.rfft(filtered_signal_mV)
    power_spectrum = np.square(np.abs(fft_values)) / len(filtered_signal_mV)
    cumulative_area = cumulative_trapezoid(power_spectrum, frequencies_hz, initial=0.0)
    half_total_area = cumulative_area[-1] / 2
    mdf_hz = float(np.interp(half_total_area, cumulative_area, frequencies_hz))
    return frequencies_hz, power_spectrum, mdf_hz


def create_figure(xlabel: str) -> tuple[plt.Figure, plt.Axes]:
    """Create a compact square plot with only the x-axis label visible."""
    figure, axis = plt.subplots(figsize=(FIGURE_SIZE_INCHES, FIGURE_SIZE_INCHES))
    axis.set_xlabel(xlabel, fontsize=LABEL_FONT_SIZE, labelpad=2)
    axis.set_yticks([])
    axis.set_xticks([])
    axis.tick_params(axis="both", which="both", length=0)
    axis.spines[["top", "right", "left"]].set_visible(False)
    return figure, axis


def save_figure(figure: plt.Figure, filename: str) -> None:
    figure.tight_layout(pad=0.25)
    figure.savefig(OUTPUT_DIRECTORY / filename, dpi=PLOT_DPI)
    plt.close(figure)


def save_raw_plot(data_frame: pd.DataFrame) -> None:
    figure, axis = create_figure("s")
    axis.plot(data_frame["time_s"], data_frame["emg_mV"], color="#4C78A8", linewidth=0.4)
    axis.axhline(0, color="black", linewidth=0.5)
    axis.plot(data_frame["time_s"], data_frame["emg_mV"], color="#4C78A8", linewidth=0.7)
    save_figure(figure, "01_raw_emg.png")


def save_filtered_plot(data_frame: pd.DataFrame) -> None:
    figure, axis = create_figure("s")
    axis.plot(data_frame["time_s"], data_frame["emg_mV"], color="#4C78A8", linewidth=0.4)
    axis.axhline(0, color="black", linewidth=0.5)
    axis.plot(data_frame["time_s"], data_frame["filtered_emg_mV"], color="#59A14F", linewidth=0.7)
    save_figure(figure, "02_filtered_emg.png")


def save_rms_plot(data_frame: pd.DataFrame, rms_data_frame: pd.DataFrame) -> None:
    figure, axis = create_figure("s")
    axis.plot(data_frame["time_s"], data_frame["emg_mV"], color="#59A14F", linewidth=0.4)
    axis.axhline(0, color="black", linewidth=0.5)
    for row in rms_data_frame.itertuples(index=False):
        axis.hlines(row.rms_mV, row.window_start_s, row.window_end_s, color="#F22B2B", linewidth=1.0)
    save_figure(figure, "03_rms_emg.png")


def save_fft_plot(
    frequencies_hz: np.ndarray,
    power_spectrum: np.ndarray,
    mdf_hz: float,
    sampling_rate_hz: int,
) -> None:
    figure, axis = create_figure("Hz")
    axis.plot(frequencies_hz, power_spectrum, color="#59A14F", linewidth=0.7)
    mdf_power = float(np.interp(mdf_hz, frequencies_hz, power_spectrum))
    axis.fill_between(
        frequencies_hz,
        power_spectrum,
        where=frequencies_hz <= mdf_hz,
        color="#59A14F",
        alpha=0.25,
    )
    axis.axvline(mdf_hz, color="red", linestyle="--", linewidth=1)
    axis.annotate(
        "MDF",
        xy=(mdf_hz, mdf_power),
        xytext=(mdf_hz + 40, mdf_power * 1.25),
        arrowprops={"arrowstyle": "->", "color": "red", "lw": 0.5},
        color="red",
        fontsize=ANNOTATION_FONT_SIZE,
    )
    axis.set_xlim(0, sampling_rate_hz / 2)
    save_figure(figure, "04_fft_mdf.png")


if __name__ == "__main__":
    OUTPUT_DIRECTORY.mkdir(exist_ok=True)
    emg_data_frame, sampling_rate_hz = load_emg_data(INPUT_PATH)
    filtered_emg_mV = bandpass_filter(emg_data_frame["emg_mV"].to_numpy(), sampling_rate_hz)
    emg_data_frame["filtered_emg_mV"] = filtered_emg_mV
    rms_data_frame = calculate_rms(filtered_emg_mV, sampling_rate_hz)
    frequencies_hz, power_spectrum, mdf_hz = calculate_mdf(filtered_emg_mV, sampling_rate_hz)

    emg_data_frame.to_csv(OUTPUT_DIRECTORY / "emg_data_frame.csv", index=False, encoding="utf-8-sig")
    rms_data_frame.to_csv(OUTPUT_DIRECTORY / "rms_values.csv", index=False, encoding="utf-8-sig")
    save_raw_plot(emg_data_frame)
    save_filtered_plot(emg_data_frame)
    save_rms_plot(emg_data_frame, rms_data_frame)
    save_fft_plot(frequencies_hz, power_spectrum, mdf_hz, sampling_rate_hz)

    print(f"Data frame: {OUTPUT_DIRECTORY / 'emg_data_frame.csv'}")
    print(f"RMS values: {OUTPUT_DIRECTORY / 'rms_values.csv'}")
    print(f"MDF: {mdf_hz:.2f} Hz")







