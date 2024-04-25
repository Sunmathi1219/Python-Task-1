# Write a program that takes a sting and return a string with all of the vowels removed.

String="I am a robot"

vowels="aeiouAEIOU"

result=""
#This line create a empty string

for character in String:
    if character not in vowels:
     #checks if the current chatacter is a vowel using the in operator

     result+=character #if the character not a vowel,it adds the character to the result string

print(result)   
