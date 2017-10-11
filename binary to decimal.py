import string


x = int(input("Please input:"))
z = x*2
list = []
newlist = []

while z>=2:
    z = z//2
    list.append(z)

list.reverse()

for z in list:
    if z%2 == 0:
        newlist.append(0)
    else:
        newlist.append(1)

newlist = [''.join(map(str,newlist))]
str_convert = ''.join(newlist)
print(str_convert)
