#author: Mitesh Chakma
#email: miteshchakma@gmail.com

#data courtesy : Sorry, I forgot where I downloaded this data from
#purpose : Educational

#I am trying to manipulate and trying to read json file using json library and
# trying to make a dictionary which will not only give the definations of the
#desired word but also try to push the similar words [if there is any typing error]

#importing libraries
import json
from difflib import get_close_matches


#importing data file
data = json.load(open("data.json"))

def translate(word):
    #as the data file contains all the definations in lowercase
    #we need to convert asking word into lowercase
    word= word.lower()
    # finding if the word in data dictionary
    if word in data:
        #if found return the defination
        return data[word]
    #search for probable word match
    elif len(get_close_matches(word, data.keys())) > 0 :
        #if found replace the probable match word and ask the user
        #if want to replace with the mistyped one
        yn=input("Did you mean %s instead? Enter Y if yes , or N if no." % get_close_matches(word,data.keys())[0])
        #if "yes" return the word and show the defination/meaning
        if yn =="Y" or yn=="y":
            return data[get_close_matches(word,data.keys())[0]]
        #if not found pass not found in the system
        elif yn=="N" or yn=="n":
            return "Word not found in the system"
        else:
            return "System cant understand the word"
    else:
        return "Word not found!"

word = input("Enter your word:")

#print(translate(word))

output = translate(word)
i=1
#showing all available definations
output = translate(word)
if type(output) == list:
    for item in output:
        print("def",i,":",item)
        i+=1
else:
    print(output)
