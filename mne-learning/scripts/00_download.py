# scripts/00 run with: uv run python scripts/00_download.py
import mne
from pathlib import Path

data_dir = Path.home() / "thesis" / "mnedata"
data_dir.mkdir(parents=True, exist_ok=True)
mne.set_config("MNE_DATA", str(data_dir))
print(mne.datasets.sample.data_path()) # MEG + EEG auditory/visual study
print(mne.datasets.mtrf.data_path()) # Lalor-lab speech EEG used for TRFs