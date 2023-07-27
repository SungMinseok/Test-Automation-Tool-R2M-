from 트리거 import *

# Read the content of target.txt
with open('트리거텍스트2.txt', 'r',encoding='utf-8') as file:
    lines = file.readlines()

# Initialize an empty namespace for variable storage
#namespace = {}  # Include the functions in the namespace

# Execute each line as Python code
for line in lines:
    for i in range(0,5):
        exec(line)
    #line = f'{line}'
    #eval(f'트리거.{line}')#, namespace)
    #eval(line.strip())#, namespace)