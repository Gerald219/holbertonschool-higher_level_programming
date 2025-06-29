from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
result = convert_csv_to_json(csv_file)

if result:
    print(f"Data from {csv_file} has been converted to data.json")
else:
    print(f"Failed to convert {csv_file}")
