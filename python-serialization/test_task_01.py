from task_01_pickle import CustomObject

# Create an instance of CustomObject
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize the object to a file
obj.serialize("object.pkl")
print("\nObject serialized successfully.")

# Deserialize the object from the file
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
if new_obj:
    new_obj.display()
else:
    print("Failed to load the object.")
