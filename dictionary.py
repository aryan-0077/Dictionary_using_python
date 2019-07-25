import json
from difflib import get_close_matches

data = json.load(open("data.json"))

# SequenceMatcher(None , "rain" ,"rainn")
#

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word , data.keys())) > 0:
        yn = input("Did u mean %s instead ? Enter Y if Yes or N if No: " % get_close_matches(word , data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or yn =="n":
            return "The word doesn't exist please double check it"
        else:
            return "We didn't understand your Entry"
    else:
        return "The word is not in this Dictionary"

word = input("Enter word for which u need Meaning: ")

#print(translate(word))

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)