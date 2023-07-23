with open('트리거텍스트.txt', 'r',encoding='utf-8') as file:
    lines = file.readlines()

output_code = []
current_iteration = 0
in_repeat_block = False

for line in lines:
    line = line.strip()
    
    if line.startswith('반복시작'):
        current_iteration = int(line.split('(')[1].split(')')[0])
        in_repeat_block = True
        output_code.append(f'for i in range(0, {current_iteration}):')
        
    elif line.startswith('반복끝'):
        if in_repeat_block:
            in_repeat_block = False
            output_code.append('')  # Add an empty line to separate repeat blocks
        
    else:
        if in_repeat_block:
            output_code.append(f"{'    ' * (current_iteration + 1)}trigger.{line}")
        else:
            output_code.append(f'trigger.{line}')

output_code = '\n'.join(output_code)

# Output the generated Python code
print(output_code)
with open('트리거코드변환결과.txt', 'w',encoding='utf-8') as output_file:
    output_file.write(output_code)