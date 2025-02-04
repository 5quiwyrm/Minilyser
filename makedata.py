inqr = input("corpus name (without extension): ")

try:
    corpus_file = open(f"corpora\\{inqr}.txt", 'r', encoding = 'u16')
except:
    raise Exception(f"There is no corpus in the corpora directory named {inqr}.txt!")

def unshift(inpt: str):
    ret = ''
    for c in inpt:
        if c in '`1234567890-=vlndkjwou,[]\\tsrhfgcaei;\nzxpb\'myq/':
            ret += c
        else:
            try:
                ret += '`1234567890-=vlndkjwou,[]\\tsrhfgcaei;\nzxpb\'myq/'['~!@#$%^&*()_+VLNDKJWOU<{}|TSRHFGCAEI:ZXPB"MYQ?>'.index(c)]
            except:
                pass
    return ret

try:
    read = corpus_file.read()
except:
    corpus_file = open(f"corpora\\{inqr}.txt", 'r', encoding = 'u8')
    read = corpus_file.read()

corpus = unshift(read)
corpus_file.close()

unigram_freqs = {}
alphas = 0
for char in corpus:
    if char in unigram_freqs.keys():
        unigram_freqs[char] += 1
    else:
        unigram_freqs.update({char : 1})
    if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
        alphas += 1
for char in unigram_freqs.keys():
    unigram_freqs[char] /= alphas

bigram_freqs = {}
nonspacebigrams = 0
for i in range(len(corpus) - 1):
    bigram = corpus[i : i + 2]
    if bigram in bigram_freqs.keys():
        bigram_freqs[bigram] += 1
    else:
        bigram_freqs.update({bigram : 1})
    if all(c.lower() in 'abcdefghijklmnopqrstuvwxyz' for c in bigram):
        nonspacebigrams += 1
for bigram in bigram_freqs.keys():
    bigram_freqs[bigram] /= nonspacebigrams

trigram_freqs = {}
for i in range(len(corpus) - 2):
    trigram = corpus[i : i + 3]
    if trigram in trigram_freqs.keys():
        trigram_freqs[trigram] += 1
    else:
        trigram_freqs.update({trigram : 1})
for trigram in trigram_freqs.keys():
    trigram_freqs[trigram] /= (len(corpus) - 2)

corpusdatafile = open(f"corporadata\\{inqr}data.py", 'w', encoding = 'utf-8')
corpusdatafile.write("unigram_freqs = " + str(unigram_freqs) + '\n')
corpusdatafile.write("bigram_freqs = " + str(bigram_freqs) + '\n')
corpusdatafile.write("trigram_freqs = " + str(trigram_freqs) + '\n')
corpusdatafile.close()

