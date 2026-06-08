# #write a program to input a sentence from user and count the number of special characters in the sentence 
sentence = input("Enter a sentence: ")
special_characters = "!@#$%^&*()_+-=[]}{|;':\",.<>/?`~"
count = 0
for char in sentence:
    if char in special_characters:
        count += 1
print("Number of special characters:", count)
