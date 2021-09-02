print("Remove Duplicate Letter in Sentence".center(75, "="))
remove = input("Input Kalimat : ")
print(' '.join(dict.fromkeys(remove.split())))
