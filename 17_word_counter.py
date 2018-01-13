string = input("Please enter string you want words counted in: \n ")
# counts only unique words
res = list(set(string.split(' ')))
print(len(res))
