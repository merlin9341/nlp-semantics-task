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

#These resuls make sense:
#-Where the same token is compared the similarity is 1.0 they are the same
#-The two animals score high when compared as do the two fruit
#-The aimals and fruit score low when compared to each other
#-The monkey has a higher score when comapered to the banana than the cat, monkeys are know to eat bananas so the words are assosiated

#Line break
print()

#for my example the 4 words are set
new_tokens = nlp("Glacier Lighthouse Flamingo Bear Skier Mountain Parrot Jungle")

#I will use tabulate to display the results in a clearer manner
from tabulate import tabulate

#list for table made using list comprehension
similarity_table = [[str(token1)] + [str(token1.similarity(token2)) for token2 in new_tokens] for token1 in new_tokens]
print(tabulate(similarity_table, headers= ["Word"] + [token_title for token_title in new_tokens], tablefmt="grid"))