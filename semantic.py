#Task 38 - Semantic Similarity (NLP) - Task 1

#modual is imported and nlp defined
import spacy

nlp = spacy.load("en_core_web_md")

#define words to be used using the nlp
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

#print out the similarity between pairs of words
print(word1.similarity(word2))
print(word2.similarity(word3))
print(word3.similarity(word1))

#now all combinations are attempted in a loop
tokens = nlp("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(f"{token1} vs {token2} similarity = {token1.similarity(token2)}")

#These 