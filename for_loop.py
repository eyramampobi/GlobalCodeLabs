for i in range(1,11):
    print (i)
    
print ("\n")
    
for j in [1, 2, 3]:
    print (j)
    
print ("\n")
    
for x in range (1,4):
    print (x)

print ("\n")

for y in range (0,19):
    print (y)

print ("\n")

def astroid():
    for x in range(1,5):
        print("****")
astroid()

print ("\n")

def meteor2(num):
    var = "*"
    for x in range(0,num):
        #print("The current index is ",x)
        if x <= num/2 :
            print (x*var)
        else:
            print ((num-x)*var)
        
meteor2(8)

#using the for each method
def search(word):
    j = 0
    for char in word:
        if char == "a":
         j = j + 1
        else:
         j = j
    if j >= 1:
        print("True")
    else:
        print("False")
        
search("bagel")

#using a contain set method
def search1(word):
    print (word.__contains__("a"))
    
search1("bagel")
        

