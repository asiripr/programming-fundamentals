print("Enter a text, I will show the word count")
text = input("Type here: ")
myList = text.split() # splits the string into a list
print("There ",len(myList)," words in your sentence.")