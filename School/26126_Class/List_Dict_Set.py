#Health reading LIST
temps = [36.5,37.0,38.5,37.2]
first = temps[0] #access by index

#Patient info DICT
patient = {"name":"Alice","age":30,"temp":37.5}
name = patient["name"] #You use he lookup

#Unique patient IDS SET
patient_ids = {101,102,103,101} 
#Duplicate gets removed
print(len(patient_ids))
if 101 in patient_ids:
    print("Patients exists!")