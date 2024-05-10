print("Enter a sentence, I will show the word count")
sentence = input("Type here: ")
myList = sentence.split() # splits the string into a list
print("There ",len(myList)," words in your sentence.")