# Write your solution here


def  factorials(n: int):
    dic = {}
    dic[1] = 1
    for i in range(2, n+1):
        dic[i] = dic[i-1] * i
    return dic



if __name__ =="__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
    