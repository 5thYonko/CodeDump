#loop = True

#while loop:
    #b_string = input("Enter a the valid binary string:")
    #if len(b_string) == 8:
        #for i in range(b_string):
            #if b_string[i] == 0 or 1:
                #print("Ok")
            #else:
                #print("string is invalid")

# attempt 2:

def b_string():
    s = {0,1}
    num = input("Enter the binary string:")
    while len(num) == 8:
        for i in range(num):
            if i in s:
                pass
            else:
                print("Invalid string combination")

#b_string()

# attempt 3

# Just some bug needs fixing else it works
# mostly
def Check_Str():
    b_String = input("Enter the string:")
    while len(b_string) == 8:
        count = 0
        x = "01"
        for i in b_string:
            if i not in x:
                count =1
                break
            else:
                pass
            if count:
                print("acceptable")
            else:
                print("Invalid")

Check_Str()

