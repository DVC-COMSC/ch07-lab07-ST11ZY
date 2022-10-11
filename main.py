
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
numbers2=[]
numbers3=[]
x=len(numbers1)
i=0
y=0
z=0
while i<x:
	numbers1[i] = int(numbers1[i])
	i=i+1
while y<x:
	if y%2==0:
		numbers2.append(numbers1[y])
	y=y+1
while z<x:
	if z%2==1:
		numbers3.append(numbers1[z])
	z=z+1
print("The list numbers:",numbers3)
print("The list for even index elements",numbers2)
