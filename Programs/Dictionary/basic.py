# dictionary: A dictionary is a data structure in Python that stores data in key–value pairs.
# Each value is accessed using its unique key.

# A dictionary is an unordered, mutable collection of elements where each element is stored as a 
# key : value pair.
# syntax:
            # dictionary_name = {
            #     key1: value1,
            #     key2: value2,
            #     key3: value3
            # }

# Ex: 
student = {
    "name": "Avani",
    "age": 21,
    "course": "BCA"
}
print(student["name"])
student["age"] = 22
print(student)