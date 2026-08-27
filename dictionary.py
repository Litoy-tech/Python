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

#for key, value in student_info.items():
#    print(f"Your {key} is {value}")
student_info["address"] = "Mingla"
student_info["Program"] = "BSIT"
student_info["ID"] = "123"
print(student_info)

#print(student_info)
#del student_info["ID"]
#print(student_info)

for info in student_info:
    print(f"My {info} is {student_info[info]}")

student_info.clear()
print(student_info)