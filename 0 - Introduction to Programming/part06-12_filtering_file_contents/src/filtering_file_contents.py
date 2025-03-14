# Write your solution here
def filter_solutions():
    input_file = "solutions.csv"
    correct_file = "correct.csv"
    incorrect_file = "incorrect.csv"
    
    correct_lines = []
    incorrect_lines = []
    
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(";")
                if len(parts) != 3:
                    continue
                
                name, problem, result = parts
                
                try:
                    correct_result = eval(problem)
                    if correct_result == int(result):
                        correct_lines.append(line)
                    else:
                        incorrect_lines.append(line)
                except:
                    incorrect_lines.append(line)
        
        with open(correct_file, "w", encoding="utf-8") as file:
            file.write("\n".join(correct_lines) + "\n")
        
        with open(incorrect_file, "w", encoding="utf-8") as file:
            file.write("\n".join(incorrect_lines) + "\n")
        
    except FileNotFoundError:
        print("The file solutions.csv was not found.")

if __name__ == "__main__":
    filter_solutions()
