from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

# Sample data
data = {
    "name": "Alice",
    "age": 28,
    "city": "San Francisco"
}

# Serialize the data
serialize_and_save_to_file(data, "data.json")
print("Data serialized successfully.")

# Load the data
loaded_data = load_and_deserialize("data.json")
print("Data loaded successfully:")
print(loaded_data)
