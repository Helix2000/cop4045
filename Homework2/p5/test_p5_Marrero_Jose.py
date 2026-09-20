import tempfile
import unittest
from datetime import datetime
from pathlib import Path
# Step E
from p5_Marrero_Jose import (
    read_observations,
    station_statistics,
    write_statistics,
)


class TestWeatherObservations(unittest.TestCase):
    def test_multiple_stations_and_negative_temperatures(self):
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "observations.csv"
            filename.write_text(
                "North,09:00:00 AM 04/20/2026,-12.5\n"
                "South,09:00:00 AM 04/20/2026,80.0\n"
                "North,09:00:00 AM 04/19/2026,-20.0\n",
                encoding="utf-8",
            )

            observations, errors = read_observations(filename)

        self.assertEqual(errors, [])
        self.assertEqual(set(observations), {"North", "South"})
        self.assertEqual(observations["North"][0][1], -20.0)
        self.assertEqual(observations["North"][1][1], -12.5)

    def test_duplicate_observation_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "duplicates.csv"
            filename.write_text(
                "Station A,09:00:00 AM 04/20/2026,70.0\n"
                "Station A,09:00:00 AM 04/20/2026,72.0\n",
                encoding="utf-8",
            )

            observations, errors = read_observations(filename)

        self.assertEqual(len(observations["Station A"]), 1)
        self.assertEqual(errors, [(2, "duplicate station/date")])

    def test_invalid_temperature_ranges_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "ranges.csv"
            filename.write_text(
                "Station A,09:00:00 AM 04/20/2026,-100.1\n"
                "Station B,09:00:00 AM 04/20/2026,150.1\n"
                "Station C,09:00:00 AM 04/20/2026,150.0\n",
                encoding="utf-8",
            )

            observations, errors = read_observations(filename)

        self.assertEqual(set(observations), {"Station C"})
        self.assertEqual(errors, [
            (1, "temperature out of range"),
            (2, "temperature out of range"),
        ])

    def test_station_statistics_are_calculated(self):
        observations = {
            "Station A": [
                (datetime(2026, 4, 19), -10.0),
                (datetime(2026, 4, 20), 20.0),
                (datetime(2026, 4, 21), 30.0),
            ],
            "Station B": [(datetime(2026, 4, 19), 5.0)],
        }

        self.assertEqual(
            station_statistics(observations),
            {
                "Station A": (-10.0, 30.0, 40.0 / 3.0),
                "Station B": (5.0, 5.0, 5.0),
            },
        )

    def test_statistics_are_written_in_sorted_order(self):
        with tempfile.TemporaryDirectory() as directory:
            filename = Path(directory) / "statistics.csv"
            write_statistics(filename, {
                "Zulu": (1.0, 2.0, 1.5),
                "Alpha": (-10.0, 20.0, 5.0),
                "Mike": (3.0, 9.0, 6.0),
            })

            output = filename.read_text(encoding="utf-8")

        self.assertEqual(
            output,
            "Alpha,-10.0,20.0,5.0\n"
            "Mike,3.0,9.0,6.0\n"
            "Zulu,1.0,2.0,1.5\n",
        )

    def test_missing_observation_file_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_observations("file_that_does_not_exist.csv")


if __name__ == "__main__":
    unittest.main()
