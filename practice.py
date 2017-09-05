words = "It's thanksgiving day. It's my birthday,too!"

words = words.replace('day','month')

print words

x = [2,54,-2,7,12,98]

x_min = min(x)


print("min:", x_min)
print("max:", max(x))


y= ["hello",2,54,-2,7,12,98,"world"]

newlist = (y[0],y[-1])

print newlist

#Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6].
# Sort your list first. Then, split your list in half.
#Push the list created from the first half to position 0 of the list created from the second half.
#The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98].
#Stick with it, this one is tough!
z = [19,2,54,-2,7,12,98,32,10,-3,6]

lower_sort = sorted(z)



print lower_sort
