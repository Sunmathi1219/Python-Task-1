#write a program that takes a string and returns a number of unique characters in it.

def count_unique_charactes(input_string):
     
    #create a set from the input string
     unique_characters=set(input_string)
     
     #returns the size of set, which is the number of unique charactes
     return len(unique_characters)


input_string="ChennaiCity"
result=count_unique_charactes(input_string)
print(f"Number of unique charactes: {result}")




