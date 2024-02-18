# CSV Parsely - Library

## Description
This is a small *.csv syntax parsing library. It is by no means extensive or well tested. I developed it in assistance of a friend for importing *.csvs into RenPy without needing to hard-code the header values.

## When To Use
If you are just reading in *.csv files from disk and are hard-coding your schema, you should probably use the provided Python `csv` module. However, this library has a different use: it automatically parses the first line and constructs the header off strings of CSV. Therefore if you want to dynamically define the schema from the CSV file, or are generating CSV at-runtime you're then parsing this can be of benefit if you don't want to do certain workarounds like wrapping a line of text in a file-like interface.

## Usage
1. Import `import csvParsely`
2. Use `csvParsely.parse_csv(your_csv_string)` to parse an already loaded csv string into a table.
3. Alternatively, use `csvParsely.parse_csv_file(file_path)` to load and parse a csv file.
4. You now have a "data table" - a list representing each row in the CSV, with each row being a dictionary of key-values based on the CSV.
5. All set! Use it how you see fit.

## Demo
To see how to use it or just see an example, look at `example.py`. This is a super simple file that just shows the `parse_csv` function. You could alternatively use `parse_csv_file` to not do the file loading shown.

## License
MIT License.

## Copyright
Joseph M. Juma, 2024. All rights reserved.