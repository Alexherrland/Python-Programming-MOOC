# Write your solution here

def create_tuple(x: int, y: int, z: int):
    smallest = min(x, y, z)
    greatest = max(x, y, z)
    sum_of_args = x + y + z
    return (smallest, greatest, sum_of_args)


if __name__ == "__main__":
    print(create_tuple(1, 4, 7))