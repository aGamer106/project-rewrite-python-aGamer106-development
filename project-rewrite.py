def min(x, y):
    if x > y:
        return y
    else:
        return x

def max(list):
    maximum = list[0]
    for number in list:
        if maximum < number:
            maximum = number
    return maximum

def len(values_list):
    counter = 0
    for i in values_list:
        counter += 1
    return counter

def multiply(x, y):
    total = 0
    counter = 0
    while counter < y:
        total += x
        counter += 1
    return total

def pow(x, y): 
     res = 1 
     for i in range(y): 
         res *= x 
     return res 

print(min(10, 5))
print(" ")
print(max([77,48,19,17,93,90]))
print(" ")
print(multiply(5, 3))
print(" ")
print(pow(3, 3))
print(" ")
string_input = input("enter string: ")
length = len(string_input)
print("Length = ", length)
print(" ")
