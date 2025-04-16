char=input("Enter a character")
if len(char)==1:
    if char.isalpha():
        print("The character is an alphabet")
    else:
        print("The character is not an alphabet")
else:
    print("Please enter only a single charater")