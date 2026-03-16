# print all even numbers from 1 to 20 using recursion
def fun(n):
    if n>20:
        return 
    print("even: ", n)
    fun(n+2)
fun(2)

# another method
def func(n):
    if n == 21:
        return
    if n%2==0:
        print(n)
    func(n+1)
func(1)