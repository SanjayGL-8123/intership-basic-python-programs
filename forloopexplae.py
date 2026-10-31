mylist = [4.2, 5, 7, 2, 4, 84]

for i in range(len(mylist)):
    print(mylist[i], end=" ")

print("\n")

i = 1
while i <= 30:
    if i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")
    i += 1

print("\n")

k = 1
while k <= 30:
    print(k, end=" ")
    k += 1