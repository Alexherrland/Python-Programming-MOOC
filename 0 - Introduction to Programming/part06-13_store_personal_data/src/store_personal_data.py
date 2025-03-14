# Write your solution here
def store_personal_data(person: tuple):
    file_name = "people.csv"
    
    try:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"{person[0]};{person[1]};{person[2]}\n")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
