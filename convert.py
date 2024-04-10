import json
import csv
import os

def json_to_csv(json_folder_path, csv_folder_path):
    json_files = [pos_json for pos_json in os.listdir(json_folder_path) if pos_json.endswith('.json')]

    for json_file in json_files:
        try:
            with open(os.path.join(json_folder_path, json_file), 'r') as json_f:
                data = json.load(json_f)

            if isinstance(data, dict):
                data = [data]  # Wrap the dictionary in a list to handle it the same way as a list of dictionaries

            if data and isinstance(data, list) and data[0]:
                keys = data[0].keys()
                csv_file = os.path.join(csv_folder_path, f'{os.path.splitext(json_file)[0]}.csv')

                with open(csv_file, 'w', newline='') as csv_f:
                    writer = csv.DictWriter(csv_f, fieldnames=keys)
                    writer.writeheader()
                    writer.writerows(data)
            else:
                print(f"File {json_file} is empty or does not contain a JSON array.")
        except json.JSONDecodeError:
            print(f"File {json_file} contains invalid JSON.")

# Usage
json_to_csv('json_folder', 'csv_folder')