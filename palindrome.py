#write a program that takes a string and returns true if it is a palindrom,false otherwise

def is_palindrome(input_string):
    
  # remove spaces and convert to lowercase for case sensitive comparision
  string=input_string.replace(" ","").lower()

  # check if the string is equal to its revese
  return string==string[::-1]

input_string="kittenettik"
if is_palindrome(input_string):
   print("true")
else:
   print("false")