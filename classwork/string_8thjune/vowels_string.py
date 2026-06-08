# write a program to input the sentence and display the frequency of each vowel which is present in that sentence ignoring the case
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
#create a dictionary to store the frequency of each vowel
frequency = {vowel: 0 for vowel in vowels}
for char in sentence:
    if char in vowels:
        #increment the frequency of the vowel in the dictionary
        frequency[char] += 1
        #print the frequency of each vowel
for vowel, count in frequency.items():
    if count > 0:
        print("Frequency of vowel:" , vowel , " is ",count)
