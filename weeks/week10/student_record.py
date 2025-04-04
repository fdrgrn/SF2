import json

sudent_record = '{"name:: "Lucy", "year": 1. "college": "Dawson}'
#parsed_record = json.loads(sudent_record)
#print(parsed_record)

student_dict = {'name':'Lucy','year':'1',"college": 'Dawson' }
#student_record_json = json.dump(student_dict)
#print(student_record_json)

output_file = open('butterflies.json', 'w')
d = {'painted lady': 1, 'monarch': 12}
json.dump(d, output_file)