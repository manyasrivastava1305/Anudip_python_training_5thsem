# write a program to input the sentence and display the frequency of vowels which are present in that sentence ignoring the case
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print("Number of vowels:", count)
