Student_Data={1:"Ram",2:"krishna",3:"Hanuman",4:"shiva",5:"Ayyappa",6:"god",7:"behappy",8:"Ds",9:"AI",10:"you can do it"}
print(type(Student_Data))
lst_of_defaulters=[]
for i in range(1,11,2):
    lst_of_defaulters.append(Student_Data[i])
for i in Student_Data:
    if Student_Data[i] not in lst_of_defaulters:
        print(Student_Data[i])
             