import csv

class CSVWriter:
    def __init__(self):
        pass

    def write_json_to_csv(self, filename, json_to_write):
        columns = list(json_to_write[0].keys())
        with open(filename, 'w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=columns)
            writer.writeheader()
            for item in json_to_write:
                writer.writerow(item)