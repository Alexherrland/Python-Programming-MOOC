# Write your solution here

def dict_of_numbers():
    numbers_dic = {}
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    for i in range(0,100):
        if i < 10:
            numbers_dic[i] = ones[i]
        elif i < 20:
            numbers_dic[i] = teens[i-10]
        else:
            if i % 10 == 0:
                numbers_dic[i] = tens[i//10]
            else:
                numbers_dic[i] = f"{tens[i//10]}-{ones[i%10]}"



    return numbers_dic


if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers)