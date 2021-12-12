# Student marks display and sort in list
m1=int(input("Enter marks for student 1:\n"))
m2=int(input("Enter marks for student 2:\n"))
m3=int(input("Enter marks for student 3:\n"))
m4=int(input("Enter marks for student 4:\n"))
m5=int(input("Enter marks for student 5:\n"))
m6=int(input("Enter marks for student 6:\n"))
list=[m1,m2,m3,m4,m5,m6]
print("before sorted list is",list)
list.sort()
print("list of marks after sort:",list)