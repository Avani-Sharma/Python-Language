# call by value: in call by value the copied values are passed into the function as an argument
# it doesn't change the original value 
# into this only immutable objects are considered as call by value 
def fun(a):
    a = a+10
    print(a)
a = 10
fun(a)
print(a)

# call by reference: into this we basically pass the reference at the time of function call 
# into the python it is automatically done when we pass any mutable object into the function call.
# in call by reference the original object is changed when we make changes from the function.
def fun(li):
    li.append(10)
lis = [1,2,3]
fun(lis)
print(lis)