# text_file = open("E:/deep projects/labs/ai/lab1.txt")
# text = text_file.read()
# # print(type(text))
# # print("\n"+text)

# from nltk.stem import PorterStemmer
# stemmer = PorterStemmer()
# print(stemmer.stem('studies'))

# from nltk.stem import WordNetLemmatizer
# lem = WordNetLemmatizer()
# print(lem.lemmatize('studies'))

# from nltk.stem import WordNetLemmatizer
# lem = WordNetLemmatizer()
# word_list =['study','studying','studies','studied']
# for w in word_list:
#       print(lem.lemmatize(w,pos='v'))

# from nltk.stem import WordNetLemmatizer
# lem = WordNetLemmatizer()
# word_list =['studies','leaves','decreases','plays']
# for w in word_list:
#       print(lem.lemmatize(w))

# from nltk.stem import WordNetLemmatizer
# lem = WordNetLemmatizer()

# word_list =["am","is","are","was","were"]

# for w in word_list:
#       print(lem.lemmatize(w, pos ="v"))

# from nltk.stem import WordNetLemmatizer
# lem = WordNetLemmatizer()

# print(lem.lemmatize("studying", pos ="v"))
# print(lem.lemmatize("studying", pos ="n"))
# print(lem.lemmatize("studying", pos ="a"))
# print(lem.lemmatize("studying", pos ="r"))



#Pos tagging Example
sentence ="A very beutiful young lady is walking on the beach"

#Tokenizing words
token_words = word_tokenize(sentence)

for words in token_words:
    tagged_words = nltk.pos_tag(token_words)

print(tagged_words)

