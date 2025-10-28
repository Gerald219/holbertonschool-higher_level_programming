#!/usr/bin/env python3
from task_01_pickle import CustomObject

# create an object
obj = CustomObject(name="John", age=25, is_student=True)

print("Original Object:")
obj.display()

# serialize (save to file)
result = obj.serialize("object.pkl")
print("\nSaved OK?:", result)

# deserialize (load from file)
new_obj = CustomObject.deserialize("object.pkl")

print("\nDeserialized Object:")
if new_obj is not None:
    new_obj.display()
else:
    print("Failed to load.")
