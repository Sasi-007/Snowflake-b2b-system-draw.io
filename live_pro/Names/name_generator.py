# Using readlines()
file1 = open('names.txt', 'r')
Lines = file1.readlines()

def func(value):
    return ''.join(value.splitlines())

file2 = open('modified_name.txt', 'w')  
for line in Lines:
    name="'"+line+"',"
    file2.writelines(func(name))

file2.close()
file1.close()