# Write your solution here
def run(program):
    variables = {chr(i): 0 for i in range(65, 91)}
    labels = {}
    output = []
    i = 0
    
    for index, line in enumerate(program):
        if line.endswith(":"):
            labels[line[:-1]] = index
    
    def get_value(val):
        return variables[val] if val in variables else int(val)
    
    while i < len(program):
        parts = program[i].split()
        if parts[0] == "PRINT":
            output.append(get_value(parts[1]))
        elif parts[0] == "MOV":
            variables[parts[1]] = get_value(parts[2])
        elif parts[0] == "ADD":
            variables[parts[1]] += get_value(parts[2])
        elif parts[0] == "SUB":
            variables[parts[1]] -= get_value(parts[2])
        elif parts[0] == "MUL":
            variables[parts[1]] *= get_value(parts[2])
        elif parts[0] == "JUMP":
            i = labels[parts[1]]
            continue
        elif parts[0] == "IF":
            left, op, right = get_value(parts[1]), parts[2], get_value(parts[3])
            condition = {
                "==": left == right,
                "!=": left != right,
                "<": left < right,
                "<=": left <= right,
                ">": left > right,
                ">=": left >= right
            }[op]
            if condition:
                i = labels[parts[5]]
                continue
        elif parts[0] == "END":
            break
        i += 1
    return output
