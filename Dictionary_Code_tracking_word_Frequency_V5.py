# Write your code here :-)
Lyrics = "Hey jude, don't make it bad. Take a sad song and make it better. Remember to let her into your heart, Then you can start to make it better. Hey jude, don't be afraid. You were made to go out and get her. The minute you let her under your skin, Then you begin to make it better. And anytime you feel the pain, hey jude, refrain, Don't carry the world upon your shoulders. For well you know that it's a fool who plays it cool By making his world a little colder.  Hey jude, don't let me down. You have found her, now go and get her. Remember to let her into your heart, Then you can start to make it better.  So let it out and let it in, hey jude, begin, Youre waiting for someone to perform with. And don't you know that it's just you, hey jude, you'll do, The movement you need is on your shoulder.  Hey jude, don't make it bad. Take a sad song and make it better. Remember to let her under your skin, Then you'll begin to make it Better better better better better better, oh. Na na na na na ,na na na, hey jude..."
############function that takes song lyrics that splits them up into a list and converts them to lower case ##########


import string


############function that iterates through song words and counts their frequency##########
def Lyric_Frequency(song_words_list):

    myDictionary = {}
    for word in song_words_list:
        #print (word)
        if word in myDictionary:#Iterates through Dictionary
            myDictionary[word] +=1 #Checks the Key in the dictionary. If word already exists then increase frequency by 1
            #print (myDictionary)

        else:
            myDictionary[word]=1 #if word is not present in dictionar this line will add that word to the dictionary
            #print (myDictionary)
    #print (myDictionary)
    return myDictionary


############function that iterates through dictionary of values creates a list##########
def frequency(myDictionary):
    values = myDictionary.values()
    values = sorted(values)
    #print(values)
    return values


############function that iterates through the values to find the biggest##########
def most_frequent(values):
    #print (values)
    #this little snippet removes the biggest value in lyrics which will always be the empty space between words
    values_length = len(values)
    biggest_number_list = values[0:values_length]
    #print (biggest_number_list)
    return biggest_number_list

    biggest_value = max(biggest_number_list)
    return biggest_value
    print ("the biggest value in the biggest_number list is ",bigest_value)




####################################################################################################################



#chosen song lyrics
song_lyrics =  "Hey jude, don't make it bad. Take a sad song and make it better. Remember to let her into your heart, Then you can start to make it better. Hey jude, don't be afraid. You were made to go out and get her. The minute you let her under your skin, Then you begin to make it better. And anytime you feel the pain, hey jude, refrain, Don't carry the world upon your shoulders. For well you know that it's a fool who plays it cool By making his world a little colder.  Hey jude, don't let me down. You have found her, now go and get her. Remember to let her into your heart, Then you can start to make it better.  So let it out and let it in, hey jude, begin, Youre waiting for someone to perform with. And don't you know that it's just you, hey jude, you'll do, The movement you need is on your shoulder.  Hey jude, don't make it bad. Take a sad song and make it better. Remember to let her under your skin, Then you'll begin to make it Better better better better better better, oh. Na na na na na ,na na na, hey jude..."

########################remove punctuation####################################
#String methods .maketrans() and .translate() that takes out all the punctuation
punctuation_dictionary = {".":None, "'": None, ",":None} #None value deletes the key value
table_Values_for_ASCII = song_lyrics.maketrans(punctuation_dictionary)
print (table_Values_for_ASCII)

song_lyrics_no_punctuation = song_lyrics.translate(table_Values_for_ASCII)
#print(song_lyrics_no_punctuation)


song_words_list = song_lyrics_no_punctuation.split()
#print (song_words_list)

#####################convert all words to lower case############################
count = -1
for x in song_words_list:
    count+=1
    x = x.lower()
    song_words_list[count]= x
print (song_words_list)
#################################################################################

########################################Code#############################################
#print (Lyric_Frequency(Lyrics))#prints off Dictionary of keys with their frequency values


myDictionary = (Lyric_Frequency(song_words_list)) #calls a function that creates a variable for the now updated dictionary
#print (myDictionary)

#print(frequency(myDictionary))#Dictionary with its values passed into function to create list of values only

values_list = (frequency(myDictionary))#creates a variable for the list of frequency values
print (values_list)


biggest_number = max(values_list)
print ("The bigesst value in the values_list is ", biggest_number)


for key in myDictionary:
    if myDictionary[key]== biggest_number:
        print("The most frequent word in the song is '" ,key,"'")

