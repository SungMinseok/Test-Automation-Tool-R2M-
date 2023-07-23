import 트리거

# Read the content of target.txt
with open('트리거텍스트.txt', 'r',encoding='utf-8') as file:
    lines = file.readlines()

# Initialize an empty namespace for variable storage
namespace = {}  # Include the functions in the namespace

# Execute each line as Python code
for line in lines:
    line = f'트리거.{line}'
    #eval(f'트리거.{line}')#, namespace)
    eval(line.strip())#, namespace)