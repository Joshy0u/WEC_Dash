from pathlib import Path

import pandas as pd

import LD_Parsing.ldparser.ldparser as ldparser


def ld_to_dataframe(file_path: str | Path) -> pd.DataFrame:
	ld_file = ldparser.ldData.fromfile(str(file_path))
	return pd.DataFrame({chan.name: chan.data for chan in ld_file.channs})


def export_ld_to_csv(file_path: str | Path, output_csv: str | Path | None = None) -> Path:
	file_path = Path(file_path)
	if output_csv is None:
		output_csv = file_path.with_suffix(".csv")
	output_csv = Path(output_csv)

	df = ld_to_dataframe(file_path)
	df.to_csv(output_csv, index=False)
	return output_csv


def export_ld_directory(input_dir: str | Path, output_dir: str | Path | None = None) -> list[Path]:
	input_dir = Path(input_dir)
	output_dir = Path(output_dir) if output_dir else input_dir
	output_dir.mkdir(parents=True, exist_ok=True)

	exported: list[Path] = []
	for ld_file in input_dir.glob("*.ld"):
		exported.append(export_ld_to_csv(ld_file, output_dir / f"{ld_file.stem}.csv"))
	return exported


if __name__ == "__main__":
	# Example usage:
	# export_ld_to_csv(r"C:\path\to\file.ld")
	# export_ld_directory(r"C:\path\to\folder")
	pass