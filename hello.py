def add(x, y):
    return x + y


result = add(1, 2)
#this print is OK in python 3.6 and above. It was not when the 
#coursera video was made and azure supported 3.5 and below.
#anyhow, how, we have both print statements in here because we were following along.

#print(f"this is the sum: 1,2, {result}")
print("This is the sum: 1,2 %s", result)