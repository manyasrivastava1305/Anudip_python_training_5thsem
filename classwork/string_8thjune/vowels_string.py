# write a program to input the sentence and display the frequency of each vowel which is present in that sentence ignoring the case
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
a=e=i=o=u=0
for char in sentence:
    if char in vowels:
        if char in "a" or char in "A":
            a += 1
        elif char in "e" or char in "E":
            e += 1
        elif char in "i" or char in "I":
            i += 1
        elif char in "o" or char in "O":
            o += 1
        elif char in "u" or char in "U":
            u += 1
if a > 0:
    print("Frequency of vowel 'a':", a) 
if e > 0:
    print("Frequency of vowel 'e':", e)
if i > 0:
    print("Frequency of vowel 'i':", i)
if o > 0:
    print("Frequency of vowel 'o':", o)
if u > 0:
    print("Frequency of vowel 'u':", u)
