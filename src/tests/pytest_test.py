import pytest, json

#Reading data.json
with open("./../../config/data.json") as file:
    data = json.load(file)
file.close()

#Create a list of tuple form this JSON data
tuple_data = ()
final_list = []

def nested_dict(val):
    data = dict(val)
    for key, val in data.items():
        if val is dict:
            nested_dict(val)
        else:
            tuple_data = [v for k, v in val.items()]
        
        mydata = tuple(tuple_data)
        final_list.append(mydata)    
        
#Calling the nested_dic funtion to generate list of tuple form data.json
nested_dict(data)

#Testing using parameterize
@pytest.mark.parametrize("name, city, job", final_list)
def test_rochak(name, city, job):
    assert(name == "rochak")
    assert(city == "pune")
    assert(job == "engineer")