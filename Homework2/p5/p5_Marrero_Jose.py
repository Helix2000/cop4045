#Name: Jose Marrero
# Z Number: Z23816617
import csv
import sys
from datetime import datetime

# Step A
def read_observations(filename: str) -> tuple[dict[str, list[tuple[datetime, float]]], list[tuple[int, str]]]:
	"""Read weather observations and report invalid input lines."""
	observations = {}
	errors = []
	seen = set()

	with open(filename, "r", newline="", encoding="utf-8") as input_file:
		csv_reader = csv.reader(input_file)

		for line_number, row in enumerate(csv_reader, start=1):
			if len(row) != 3:
				errors.append((line_number, "malformed line"))
				continue

			station, date_text, temperature_text = (field.strip() for field in row)
			if not station or not date_text or not temperature_text:
				errors.append((line_number, "malformed line"))
				continue

			try:
				date = datetime.strptime(date_text, "%I:%M:%S %p %m/%d/%Y")
			except ValueError:
				errors.append((line_number, "malformed date"))
				continue

			try:
				temperature = float(temperature_text)
			except ValueError:
				errors.append((line_number, "invalid temperature"))
				continue

			if not -100.0 <= temperature <= 150.0:
				errors.append((line_number, "temperature out of range"))
				continue

			observation_key = (station, date)
			if observation_key in seen:
				errors.append((line_number, "duplicate station/date"))
				continue

			seen.add(observation_key)
			observations.setdefault(station, []).append((date, temperature))

	for station_observations in observations.values():
		station_observations.sort(key=lambda observation: observation[0])

	return observations, errors

# STep B
def station_statistics(observations: dict[str, list[tuple[datetime, float]]]) -> dict[str, tuple[float, float, float]]:
	"""Return each station's minimum, maximum, and mean temperature."""
	statistics = {}

	for station, station_observations in observations.items():
		temperatures = [temperature for _, temperature in station_observations]
		if temperatures:
			statistics[station] = (
				min(temperatures),
				max(temperatures),
				sum(temperatures) / len(temperatures),
			)

	return statistics

# Step C
def station_outliers(observations: dict[str, list[tuple[datetime, float]]]) -> dict[str, tuple[datetime, float, float]]:
	"""Return stations whose latest temperature is above their mean."""
	statistics = station_statistics(observations)
	latest = {
		station: max(station_observations, key=lambda observation: observation[0])
		for station, station_observations in observations.items()
		if station_observations
	}

	return {
		station: (date, temperature, statistics[station][2])
		for station, (date, temperature) in latest.items()
		if temperature > statistics[station][2]
	}


# Step D
def write_statistics(filename: str, statistics: dict[str, tuple[float, float, float]]) -> None:
	"""Write station statistics in sorted order with one decimal place."""
	with open(filename, "w", newline="", encoding="utf-8") as output_file:
		csv_writer = csv.writer(output_file, lineterminator="\n")
		for station in sorted(statistics):
			minimum, maximum, mean = statistics[station]
			csv_writer.writerow((station, f"{minimum:.1f}", f"{maximum:.1f}", f"{mean:.1f}"))

# Step E
def main() -> None:
	"""Read observations, display results, and write station statistics."""
	if len(sys.argv) != 3:
		print("Usage: python p5_Marrero_Jose.py input_file output_file", file=sys.stderr)
		return

	input_filename, output_filename = sys.argv[1:]

	try:
		observations, errors = read_observations(input_filename)
		statistics = station_statistics(observations)
		outliers = station_outliers(observations)

		if errors:
			print("Input errors:")
			for line_number, error_message in errors:
				print(f"Line {line_number}: {error_message}")

		print("Statistics:")
		for station in sorted(statistics):
			minimum, maximum, mean = statistics[station]
			print(f"{station}: min={minimum:.1f}, max={maximum:.1f}, mean={mean:.1f}")

		print("Outliers:")
		for station in sorted(outliers):
			date, temperature, mean = outliers[station]
			print(
				f"{station}: {date.strftime('%I:%M:%S %p %m/%d/%Y')}, "
				f"temperature={temperature:.1f}, mean={mean:.1f}"
			)

		write_statistics(output_filename, statistics)
		print(f"Statistics written to {output_filename}")
		print("Jose Marrero, Z23816617")
	except (OSError, csv.Error, ValueError) as error:
		print(f"Error: {error}", file=sys.stderr)
		
# Step F

if __name__ == "__main__":
	main()


