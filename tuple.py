tup1 = ('physics', 'chemistry', 1997, 2000);
list1 = []
for i in tup1:
    if i == 1997:
        list1.append(1996)
    else:
        list1.append(i)
print (list1)
del (tup1)
tup1 = (list1)
print (tup1)



tup2 = ([10,'abc','red',786],'physics', 'chemistry', 1997, 2000);
print (tup2)