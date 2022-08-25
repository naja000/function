def reusable():
        print("this value is a reusable function 1")
        print("this value is a reusable function 2")
        print("this value is a reusable function 3")
        print("this value is a reusable function 4")
        print("____________________________________")

num=int(input("enter a number:  "))
for i in range(1,num):
    reusable()