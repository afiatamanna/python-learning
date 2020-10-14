
# for loop example
fruits=["apple","grapes", "orange", "mango"]
for i in fruits:
    print("{} is your favorite".format(i))

for number in range(1,10):
    print("number is {}".format(number))
# error code
'''day=["sunday","mon","tuesday","wednesday","friday"]
for day in range("sunday","wednesday"):
    print("today is {}".format(day))'''



# while loop example
temp=40
while temp>=33:
    print("temparature is {}".format(temp))
    temp-=1

# loop control

#break
temp=40
while temp>=33:
    print("temparature is {} deg.".format(temp))
    temp-=5
    if temp==30:
        break

# continue
for number in range(1,10):
     if number==5:
         print("skip the {}".format(number))
         continue
     print("the number is {}".format(number))

# pass
for number in range(1,11):
    if number==4:
        pass
    else:
        print("the number is showed {}".format(number))
