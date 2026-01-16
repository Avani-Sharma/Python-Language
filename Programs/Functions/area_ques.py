# write a function area (len, wid) default = 5
def area(len, wid=5):
  return len*wid
len = int(input("enter the length"))
wid = int(input("enter the width"))
area(len, wid)

print(area(len, wid))