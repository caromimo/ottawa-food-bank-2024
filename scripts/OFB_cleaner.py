"""
Module providing a class to clean OFB data.
It reads data from a CSV, runs cleaning functions on it, and writes out a new CSV.

Copyright 2024 Andy Maloney <asmaloney@gmail.com>
SPDX-License-Identifier: MIT
"""

import argparse
import csv
import pathlib

from collections import defaultdict
from typing import List


class OFB_Cleaner:
    """Class to handle cleaning of OFB data"""

    def __init__(self, input_file_name: str, output_file_name: str):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def process_q003(self, fields: List[str]) -> List[str]:
        """
        - capitalize occcurances of "prefer not to answer" and "don't know"
        """
        for index, field in enumerate(fields):
            if field == "prefer not to answer":
                fields[index] = field.capitalize()
            if field == "don't know":
                fields[index] = field.capitalize()
        return fields

    def process_q004(self, fields: List[str]) -> List[str]:
        """
        - capitalize occcurances of "prefer not to answer" and "never true"
        """
        for index, field in enumerate(fields):
            if field == "prefer not to answer":
                fields[index] = field.capitalize()
            if field == "never true":
                fields[index] = field.capitalize()
        return fields

    def process_q005(self, fields: List[str]) -> List[str]:
        """
        - capitalize occcurances of "don't know"
        """
        for index, field in enumerate(fields):
            if field == "don't know":
                fields[index] = field.capitalize()
        return fields

    def process_q006(self, fields: List[str]) -> List[str]:
        """
        - capitalize occcurances of "don't know"
        """
        for index, field in enumerate(fields):
            if field == "don't know":
                fields[index] = field.capitalize()
        return fields

    def process_q007(self, fields: List[str]) -> List[str]:
        """
        - capitalize occcurances of "don't know"
        """
        for index, field in enumerate(fields):
            if field == "don't know":
                fields[index] = field.capitalize()
        return fields

    def process_q008(self, fields: List[str]) -> List[str]:
        """
        - capitalize occcurances of "don't know"
        """
        for index, field in enumerate(fields):
            if field == "don't know":
                fields[index] = field.capitalize()
        return fields

    def normalize(self, fields: List[str]) -> List[str]:
        """
        - normalize lowercase "na" or "Na" to "NA"
        """
        for index, field in enumerate(fields):
            if field.casefold() == "na":
                fields[index] = "NA"
        return fields

    def clean(self):
        """
        Reads data from a CSV, runs cleaning functions on it, and writes out a new CSV.
        """
        rows: List[dict] = [{}]

        # open and read the input file
        with open(self.input_file_name, encoding="utf-8") as istream:
            csv_reader = csv.DictReader(istream)

            # read the data into columns since that's the way we are processing it
            print(f"Reading from {self.input_file_name}...")
            columns = defaultdict(list)
            for row in csv_reader:
                for k, v in row.items():
                    columns[k].append(v)

            # get number of rows & columns
            first_column = list(columns.values())[0]
            num_rows = len(first_column)
            num_columns = len(columns)

            print(f" ...found {num_rows} rows and {num_columns} columns")

            # process the data
            print("Cleaning the data by column...")
            for name, column in columns.items():
                # first run general normalization
                fields = self.normalize(column)
                columns[name] = fields

                if self.has_method(f"process_{name}"):
                    processing = getattr(OFB_Cleaner, f"process_{name}")
                    fields = processing(self, column)
                    columns[name] = fields

            # convert back to rows for writing
            rows = [{} for _ in range(num_rows)]

            for name, column in columns.items():
                row_index: int = 0
                for item in column:
                    rows[row_index][name] = item
                    row_index += 1

            # remove invalid rows which have an ID of "NA"
            print("Removing invalid rows...")
            rows = filter(lambda item: item["q001"] != "NA", rows)

        # remove the output file if it exists and open it for writing
        pathlib.Path(self.output_file_name).unlink(missing_ok=True)

        # write out the new CSV
        with open(self.output_file_name, encoding="utf-8", mode="w") as ostream:
            csv_writer = csv.DictWriter(
                ostream, dialect="excel", fieldnames=csv_reader.fieldnames
            )

            print(f"Writing to {self.output_file_name}...")
            csv_writer.writeheader()
            csv_writer.writerows(rows)

        print("Done")

    def has_method(self, name: str):
        """
        Checks if this class has a method named "name"
        """
        return callable(getattr(OFB_Cleaner, name, None))


if __name__ == "__main__":
    DEFAULT_INPUT_FILE = "data/neighbour_survey_clean-2024-06-14.csv"
    DEFAULT_OUTPUT_FILE = "neighbour_clean.csv"

    define_parser = argparse.ArgumentParser(
        description="Clean the OFB data.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    define_parser.add_argument(
        "--input",
        type=str,
        help="Input file path",
        default=DEFAULT_INPUT_FILE,
    )
    define_parser.add_argument(
        "--output",
        type=str,
        help="Output file path",
        default=DEFAULT_OUTPUT_FILE,
    )
    args = define_parser.parse_args()

    cleaner = OFB_Cleaner(args.input, args.output)
    cleaner.clean()
