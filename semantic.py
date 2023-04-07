#L3T12 - Compulsary Task 1.

import spacy
nlp = spacy.load('en_core_web_md')



# Example 1.
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))



# Example 2.
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
      for token2 in tokens:
            print(token1.text, token2.text, token1.similarity(token2))



# Example 3.
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
      similarity = nlp(sentence).similarity(model_sentence)
      print(sentence + " - ", similarity)

# Answer 1.
# The interesting thing about the similarities between cat, monkey, and banana 
# is that they are not very similar to each other in terms of their physical 
# characteristics or what they represent. Yet, in the context of natural language
# processing, the computer is able to understand and quantify their similarities 
# based on the patterns of their usage in language.

# my own example:
word1 = nlp("water")
word2 = nlp("juice")
word3 = nlp("rain")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


# Answer 2 - en_core_web_sm' instead of 'en_core_web_md:
#
# I noticed a difference in the similarity scores produced by the model. 
# The 'en_core_web_sm' model scored lower compared to 'en_core_web_md'. 
# As a result, it may not have the same level of accuracy or precision in 
# identifying similarities or dissimilarities between longer texts like the 
# complaints and recipes in the example code.
