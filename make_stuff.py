#texts nlp
import random
import spacy
import numpy as np
from numpy import dot
from numpy.linalg import norm
import json

words = open("1184-0.txt").read().split()
nlp = spacy.load('en_core_web_md')
text = open("1184-0.txt").read()
doc = nlp(text)

sentences = list(doc.sents)
words = [w for w in list(doc) if w.is_alpha]
entities = list(doc.ents)
noun_chunks = list(doc.noun_chunks)
document_list = list(doc)
punct = [w for w in document_list if w.pos_ == "PUNCT"]
self_punct = ["[]","(   )","()",">>>","!!!+","+-","_______","-----","::","++","&","<<<",">","//","?","| |     |","||","\\","|:"]
x = random.sample(words,1)


#glove
# cosine similarity
def cosine(v1, v2):
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

unique_words = list(set([w.text for w in words]))

def similar_words(word_to_check, source_set):
    return sorted(source_set,
                  key=lambda x: cosine(nlp.vocab[word_to_check].vector, nlp.vocab[x].vector),
                  reverse=True)

similar_words("where", unique_words)[:10]

def sentence_vector(sent):
    vec = np.array([w.vector for w in sent if w.has_vector and np.any(w.vector)])
    if len(vec) > 0:
        return np.mean(vec, axis=0)
    else:
        raise ValueError("no words with vectors found")   

def similar_sentences(input_str, num=20):
    input_vector = sentence_vector(nlp(input_str))
    return sorted(sentences,
                  key=lambda x: cosine(np.mean([w.vector for w in x], axis=0), input_vector),
                  reverse=True)[:num]



sum_sentences = []
sentence_to_check2 = "im not sure"
for item in similar_sentences(sentence_to_check2):
	generated_sentences = item.text.strip()
	sum_sentences.append(generated_sentences)

# modified_sentences = []
# for item in sum_sentences:
#     wordz = [w.text for w in item]
#     for wo in wordz:
#         wo_str = "_____ "
#         replaced = wo.replace(wo, wo_str)
#         modified_sentences.append(replaced)
#         print (replaced)
#     print (wordz)
# print (' '.join(modified_sentences))

#write files
sentc = []
sentence_to_check = "how did i"
for item in similar_sentences(sentence_to_check):
    generated_sentences = item.text.strip()
    sentc.append(generated_sentences)
    #print(generated_sentences)
    #print("")

punctuation = []
for item in random.sample(punct, 95):
	punctuation.append(item.text)

noun = []
for item in noun_chunks:
	noun.append(item.text)

with open('json_data.json', 'w') as outfile:  
    json.dump({'sentences':sentc, 'punct':punctuation, 'noun': noun}, outfile)

print("done")


# with open('testdata.txt', 'w', encoding='utf8') as outfile:
# 			outfile.write(",".join(sentences_array))