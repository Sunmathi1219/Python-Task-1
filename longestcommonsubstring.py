# write a program that takes two string and retutrn the longest common substring between them

def longest_common_substring(str1,str2):
    
    #initialize the variable to store the string
    max_length=0
    longest_substring=""

    #iteration
    for i in range(len(str1)):
        for j in range(i+1,len(str1)+1):

            # extract the current substring from s1
            substring=str1[i:j]

            # check if current substring is exist in s2
            if substring in str2:
                if len(substring)>max_length:
                    max_length=len(substring)
                    longest_substring=substring

    return longest_substring

str1="LEWSSORK"
str2="WORKHARD"
result=longest_common_substring(str1,str2)
print(f"Longest  common substring is : {result} ")