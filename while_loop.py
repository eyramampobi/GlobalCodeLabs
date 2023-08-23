print ("Numbers from 7 to 19")
i = 6
while(i < 19):
    i = i + 1
    print (i)
print("\n")

print("Even numbers from 12 to 20")
x = 10
while(x < 20):
    x = x + 2
    print (x)
print("\n")



def evens():
    num1 = int(input("Enter the lower bound: "))
    num2 = int(input("Enter the upper bound: "))
    x = num1 + 1
    while (num1<x<num2):
            if x % 2 == 0:
                print(x)
            x = x + 1
                  
evens()

def reverse_evens():
    num1 = int(input("Enter the lower bound: "))
    num2 = int(input("Enter the upper bound: "))
    x = num2 - 1
    while (num1<x<num2):
            if x % 2 == 0:
                print(x)
            x = x - 1
                  
reverse_evens()
          

    
