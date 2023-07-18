### A function that takes a list as an input and returns its sum.

def sum_list(lst):
    return sum(lst)

my_list = [1,2,3,4,5]
a= sum_list(my_list)
print(a)


### A function that takes a list as an input and returns its maximum value


def max_val(lst):
    return max(lst)

my_list = [10000,2000,300,400,5000]
b= max_val(my_list)
print(b)


### A function that takes a list as an input and returns the reverse of the list.

def reversal(lst):
    lst.reverse()
    return lst

my_list = [10,20,30,0,500]
c= reversal(my_list)
print(c)

### A function that takes a list as an input and returns the sorted form of the list.


def sort(lst):
    temp = 0
    for i in range(len(lst)):
        for j in range(i):
            if lst[j]>lst[j+1]:
                temp = lst[j]
                lst[j]=lst[j+1]
                lst[j+1] = temp 
                j += 1

    return lst

my_list = [11,9,80,50,500]
c= sort(my_list)
print(c)


### A function that takes a list as an input and returns the mean for the list.

def stats(c):
    mean = float(sum(c)/(len(c)))
    return (mean)

my_list = [20,20,40,40,40,70,70,500,600]
c= stats(my_list)
print(c)



### A function that takes a list as an input and returns the mode for the list.

def mode(List):
	counter = 0
	num = 0
	
	for i in List:
		frequency = List.count(i)
		if(frequency> counter):
			counter = frequency
			num = i

	return num

List = [2, 1, 2, 2, 1, 3, 4, 5, 6, 7, 7, 7, 7, 3, 8, 9, 10, 10]
print(mode(List))






### Enter numbers as input and return sum of array
k = int(input("Enter the value of k required: "))
array=[]
for i in range(k):
     j=int(input("Enter value at indexs required: "))
     array.append(j)

start = int(input("Enter the start value required: "))
end = int(input("Enter the end value required: "))


k = sum(array[start:end])

print (k)
