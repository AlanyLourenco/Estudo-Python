#loops idioms- com a forma como construimos loops
largest_so_far = -1
print(f'Before', largest_so_far)
for the_num in [9,41,12,3,74,15]:
    if the_num>largest_so_far:
        largest_so_far= the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)


smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)


zork=0
sum=0
print('Before', zork, sum)
for value in [9,41,12,3,74,15]:
    zork+=1
    sum=sum+value
    print(zork,value)
print('After', zork,sum,sum/zork)


foud=False
print('Before',foud)
for value in [9,41,12,3,74,15]:
    if value==3:
        foud=True
        #print(foud,value)
        #break
    else:
         foud=False
    print(foud,value)
print('After',foud)
