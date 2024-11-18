# int("1234")  # casting

# music = "classical"
# shopping_list = []
# num = 0
# name = ""
# my_name = "Prathamm"

# print (bool(music))  # True 
# print (bool(shopping_list))  # False
# print (bool(num))  # False
# print (bool(name))  # False
# print (bool(my_name))  # True

# # check "Falsy values" in slide 
# ---------------------------------------------------------------

# for choice in username eg- can use (IF statements)
user_name =  input("Please enter your chosen user name: "). strip()  # strip- strip away spaces; as " " is also counted as a character. (len=1)

if user_name:
    print (f"Welcome to your new account, {user_name}")
else:
    print("You did not enter anything")     