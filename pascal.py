from math import factorial as fact
def mohasebefac(n, k):
    number = fact(n) / (fact(k) * fact(n-k))
    return number


def pascal(n):
    row_list = []
    for row in range(n):
        for k in range(row+1):
            number = mohasebefac(row, k)
            row_list.append(int(number))
        print(row_list)
        row_list.clear()


n = int(input("Enter number of rows: "))
pascal(n)
#code by shayan hashemi