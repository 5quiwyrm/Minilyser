inqr = input("corpus name (without extension): ")

try:
    corpus_file = open(f"corpora\\{inqr}.txt", 'r', encoding = 'utf8')
except:
    raise Exception(f"There is no corpus in the corpora directory named {inqr}.txt!")

corpus = corpus_file.read()
corpus_file.close()

unigram_freqs = {}
for char in corpus:
    if char in unigram_freqs.keys():
        unigram_freqs[char] += 1
    else:
        unigram_freqs.update({char : 1})
for char in unigram_freqs.keys():
    unigram_freqs[char] /= len(corpus)

bigram_freqs = {}
for i in range(len(corpus) - 1):
    bigram = corpus[i : i + 2]
    if bigram in bigram_freqs.keys():
        bigram_freqs[bigram] += 1
    else:
        bigram_freqs.update({bigram : 1})
for bigram in bigram_freqs.keys():
    bigram_freqs[bigram] /= (len(corpus) - 1)

trigram_freqs = {}
for i in range(len(corpus) - 2):
    trigram = corpus[i : i + 3]
    if trigram in trigram_freqs.keys():
        trigram_freqs[trigram] += 1
    else:
        trigram_freqs.update({trigram : 1})
for trigram in trigram_freqs.keys():
    trigram_freqs[trigram] /= (len(corpus) - 2)

corpusdatafile = open(f"corporadata\\{inqr}data.py", 'w')
corpusdatafile.write("unigram_freqs = " + str(unigram_freqs) + '\n')
corpusdatafile.write("bigram_freqs = " + str(bigram_freqs) + '\n')
corpusdatafile.write("trigram_freqs = " + str(trigram_freqs) + '\n')
corpusdatafile.close()

