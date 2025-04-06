#Takes the filetext and counts the amount of words in a file
def get_num_words(filetext):
    text = filetext.split()
    num_words = len(text)
    return num_words

#Counts the amount of characters and returns it into a dictionary
def get_characters(filetext):
    text_dictionary = {}
    filetextlower = filetext.lower()
    for character in filetextlower:
        if character in text_dictionary:
            text_dictionary[character] += 1
        elif character not in text_dictionary:
            text_dictionary[character] = 1
    return text_dictionary
   
def sort_on(dict):
    return dict["count"]

#Sorts the above dictionary by greatest to least size
def sort_dictionary(filetext):
    dictionary_list = []
    dictionary = get_characters(filetext)
    for item in dictionary:
        tempdict = {"char": item, "count" : dictionary[item]}
        dictionary_list.append(tempdict)
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
