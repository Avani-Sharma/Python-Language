#  print the numbers from 1 to 10 using the recursion
def fun(n):
  if n==10:
    return 
  print("number is: ", n)
  fun(n+1)
fun(1)

print()

#  print the numbers from 10 to 1 using the recursion
def func(n):
    if n == 0:
        return
    print("num is: ", n)
    func(n - 1)
func(10)