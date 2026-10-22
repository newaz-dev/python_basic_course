# JSON(Java Scrippt Object Notation):

# JSON SERIALIZATION(Pyton ---->JSON):
import json
data = {
    'name' : "Newaz",
    'age' : 25,
    'address' : "Dhaka",
    'is_logged_in' : True, #'True' will be 'true'
    'test' : None # this will convert into 'null', cause javascript doesnt support None
    
}
json_string_conv = json.dumps(data, indent = 4)
print(json_string_conv)

# DESERIALIZATION: JSON ----->Python conversion:
data_2 = '{"name" : "Newaz", "age" : 25, "address" : "Dhaka", "is_logged_in" : true}'
python_dict = json.loads(data_2)
print(python_dict)
