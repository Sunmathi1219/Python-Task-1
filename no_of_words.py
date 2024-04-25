#write a program that takes a string and returns number of words in it

def count_words(string):


    #split the string into words
    words=string.split()

    #return length of words
    return len(words)

string="I Am Happy To Learn Python Program"
print(count_words(string))