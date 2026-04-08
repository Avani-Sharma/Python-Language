# Accept a password from the user; if it matches the stored one, print “Login Successful”, else “Try Again”.

password = input("enter password: ")
stored = "Avani_Sharma"
if stored == password:
    print("login successful")
else:
    print("try again")