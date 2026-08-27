#dictionary = uniqu, organized, and mutable

student_info = {
    #key       Value
    "name" : "Lito",
    "age" : "19",
    "address" : "Camp 7"
}

#print(student_info["name"])
#print(student_info["age"])
#print(student_info["address"])

#for info in student_info.items():
#    print(info)

#for value in student_info.values():
#    print(value)

#for key in student_info.items():
#    print(key)

for key, value in student_info.items():
    print(f"Your {key} is {value}")
