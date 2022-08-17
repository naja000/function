def max_of_three(a,b,c):
    sum=(a,b,c)
    return sum

num1=int(input("enter a number: "))
sum=max_of_three(num1,2,3)
print(sum)


def max_of_three(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
