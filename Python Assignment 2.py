my_list = []
print("Before append:",my_list)
my_list.append (10) 
print("After append:",my_list)
my_list.append (20) 
print("After append:",my_list)
my_list.append (30)
print("After append:",my_list)
my_list.append (40)
print("After append:",my_list)
my_list[2] = 15
print("my_list:",my_list)
my_list = [10,20,15,40]
list_2 = [50,60,70]
print("list_2:",list_2)
my_list.extend(list_2)
print("List after append:",my_list)
my_list = [10,20,30,40]
print("my_list:",my_list)
my_list.remove(40)
print("my_list after remove:",my_list)
my_list = [10,20,30,40]
print("my_list:",my_list)
my_list.sort(reverse=True)
print("my_list(Descending Order):",my_list)
my_list.sort()
print("my_list(Ascending order):",my_list)
print(my_list.index(30))

