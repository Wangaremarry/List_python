from re import M


my_list=['p','r','o','b','l','e','m']
my_list[2:3]=[]
print(my_list)
print(my_list.pop())
print(my_list.sort())
print('k' in my_list)
print('r' in my_list)

numbers=[2,3,4,5,6,7]
for x in numbers:print(x**5)
  
fruits=['apple','banana','mango','grapes']
for fruit in fruits:
    print("I like",fruit)

# Tuple

my_tuple=(1,2,3.6,[7,5])
print(my_tuple)
a,b,c,d=my_tuple
print(a)
print(d)
print(my_tuple[2],[3])
my_tuple[3][0]=9
print(my_tuple)
my_tuple[3][0]=8
print(my_tuple)

repeat=(1,2,3,4)
print((1,2,3,4)+(5,6,7,8))
print(("1,2,3,4",)*2)
print(3 in repeat)

# string
string=("programiz")
print(string[0])
print(string[-1])