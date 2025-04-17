print("Task 1")
numbs = [x for x in range(1,100) if x%3==0 and x%5!=0]
print(numbs)
print("------------------------------")
print("Task 2")
temps = [C * 9/5 + 32 for C in [0,10,20,30,40,100]]
print(temps)
print("------------------------------")
print("Task 3")
numbs = [x**2 for x in range(1,51) if x%2==0]
print(numbs)
print("------------------------------")
print("Task 4")
text = "Python is amazing and powerful language"
lngs = [len(word) for word in text.split()]
print(lngs)
print("------------------------------")
print("Task 5")
numbs = [x for x in range(2,101) if len([i for i in range(1, x+1) if x%i==0])>2]
print(numbs)
