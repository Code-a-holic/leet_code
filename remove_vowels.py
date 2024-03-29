# Check for vowels in string and remove them. If vowels are consecutive then do not remove them.

def isVowel(check_char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for j in vowels:
        if check_char == j:
            return True

input_string = input("Enter String: ")

for i in range(len(input_string)):
    # print("\n"+str(i)+"\n")
    if isVowel(input_string[i]):
        if isVowel(input_string[i+1]):
            print(input_string[i], end="")
        elif isVowel(input_string[i-1]):
            print(input_string[i], end="")
        else:
            pass
    else:
        print(input_string[i], end="")


