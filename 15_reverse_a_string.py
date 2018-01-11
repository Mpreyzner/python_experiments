string = input("Enter a string to reverse\n")

reversed = ''


for i in range(len(string) -1, -1, -1):
    reversed = reversed + string[i]

print(reversed)
