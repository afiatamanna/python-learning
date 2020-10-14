fruit=["apple", "peach","mango","mango","mango","mango"]
year=[1998, 2010,1999,1997,2007,2008]
fruit.append("pear")
print("apple" in fruit)
print("pear" in fruit)
print("grape" in fruit)
print(fruit.count("mango"))
print(fruit.count("grape"))
print(fruit.index("mango"))

print("here the list of fruits:  {}".format(fruit))

fruit.extend(year)
print("here the list of fruits:  {}".format(fruit))

year.remove(1998)
print("here the list of year:  {}".format(year))
fruit.remove(2007)
print("here the list of fruits:  {}".format(fruit))
fruit.pop(1)
print("here the list of fruits:  {}".format(fruit))
fruit.pop(-2) #2nd last remove
print("here the list of fruits:  {}".format(fruit))

year.sort()
print("here the list of year:  {}".format(year))

num=[1,2,3,4,5,6,7]
num1=[2]
print([2]*4)
print (num[2:5])
print(num[1:])
num2=[1,2,3,4,5,6,7]
print(num2[1:])

