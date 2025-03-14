# Write your solution here
# You can test your function by calling it within the following block

def greatest_number(int1,int2,int3):
    
    list_integers = [int1,int2,int3]
    return max(list_integers)
    
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)