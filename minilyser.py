corpusname = input("corpus name (without extension): ")

import os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

verbosity = 0
thumbstatsarereal = True

if len(sys.argv) > 1:
    if sys.argv[1] == '1':
        verbosity = 1
    elif sys.argv[1] == '2':
        verbosity = 2
    if len(sys.argv) > 2:
        if sys.argv[2] == 'false':
            thumbstatsarereal = False

try:
    exec(f"import corporadata.{corpusname}data as data")
except:
    raise Exception(f"The data for {corpusname} has not been generated yet, refer to README for information on how to generate data.")
print(f"{corpusname} loaded as corpora of choice")

class letter:
    def __init__(self, row, finger):
        self.row = row
        self.finger = finger
    def __str__(self):
        return f"letter({row}, {finger})"
    def hand(self):
        if self.finger in [8, 0, 1, 2, 3]:
            return "left"
        elif self.finger in [9, 4, 5, 6, 7]:
            return "right"
        else:
            return "middle"

nky = 'nokeyishere'

curr_layout = {
    'v' : letter(0, 0), 'l' : letter(0, 1), 'n' : letter(0, 2), 'd' : letter(0, 3), 'k' : letter(0, 3), 'j' : letter(0, 7), 'w' : letter(0, 7), 'o' : letter(0, 6), 'u' : letter(0, 5), ',' : letter(0, 4),
    't' : letter(1, 0), 's' : letter(1, 1), 'r' : letter(1, 2), 'h' : letter(1, 3), 'f' : letter(1, 3), 'g' : letter(1, 7), 'c' : letter(1, 7), 'a' : letter(1, 6), 'e' : letter(1, 5), 'i' : letter(1, 4), '\n' : letter(1, 4),
    'z' : letter(2, 1), 'x' : letter(2, 2), 'p' : letter(2, 3), 'b' : letter(2, 3), '\'' : letter(2, 3), 'm' : letter(2, 7), 'y' : letter(2, 7), 'q' : letter(2, 6), '/' : letter(2, 5), '.' : letter(2, 4),
    ' ' : letter(-2, 8)
}
thumb_keys = [' ']

loadlayout = input("Input a layout name to load. If you do not wish to load a layout, input nothing. \nName: ")
if loadlayout != '':
    try:
        layoutfile = open(f"layouts\\{loadlayout}.txt", 'r')
        rd = layoutfile.read()
        exec(rd)
        layoutfile.close()
    except:
        print(f"{loadlayout} does not exist yet, proceeding with default...")

usfb = 0
usfb_list = []
uusfb = 0
uusfb_list = []

infullscissor = 0
infullscissor_list = []
outfullscissor = 0
outfullscissor_list = []

inhalfscissor = 0
inhalfscissor_list = []
outhalfscissor = 0
outhalfscissor_list = []

inroll = 0
inroll_list = []
outroll = 0
outroll_list = []

for bigram in data.bigram_freqs.keys():
    if curr_layout[bigram[0]].finger == curr_layout[bigram[1]].finger and bigram[0] != bigram[1]:
        if abs(curr_layout[bigram[0]].row - curr_layout[bigram[1]].row) == 1:
            usfb += data.bigram_freqs[bigram]
            usfb_list += [[bigram, data.bigram_freqs[bigram]]]
        if abs(curr_layout[bigram[0]].row - curr_layout[bigram[1]].row) == 2:
            uusfb += data.bigram_freqs[bigram]
            uusfb_list += [[bigram, data.bigram_freqs[bigram]]]
    if abs(curr_layout[bigram[0]].row - curr_layout[bigram[1]].row) == 2 and abs(curr_layout[bigram[0]].finger - curr_layout[bigram[1]].finger) == 1:
        if curr_layout[bigram[0]].finger < curr_layout[bigram[1]].finger:
            infullscissor += data.bigram_freqs[bigram]
            infullscissor_list += [[bigram, data.bigram_freqs[bigram]]]
        else:
            outfullscissor += data.bigram_freqs[bigram]
            outfullscissor_list += [[bigram, data.bigram_freqs[bigram]]]
    if abs(curr_layout[bigram[0]].row - curr_layout[bigram[1]].row) == 1 and abs(curr_layout[bigram[0]].finger - curr_layout[bigram[1]].finger) == 1:
        if curr_layout[bigram[0]].finger < curr_layout[bigram[1]].finger:
            inhalfscissor += data.bigram_freqs[bigram]
            inhalfscissor_list += [[bigram, data.bigram_freqs[bigram]]]
        else:
            outhalfscissor += data.bigram_freqs[bigram]
            outhalfscissor_list += [[bigram, data.bigram_freqs[bigram]]]
    if curr_layout[bigram[0]].row == curr_layout[bigram[1]].row and bigram[0] != bigram[1] and curr_layout[bigram[0]].hand() == curr_layout[bigram[1]].hand():
        if curr_layout[bigram[0]].finger < curr_layout[bigram[1]].finger:
            inroll += data.bigram_freqs[bigram]
            inroll_list += [[bigram, data.bigram_freqs[bigram]]]
        else:
            outroll += data.bigram_freqs[bigram]
            outroll_list += [[bigram, data.bigram_freqs[bigram]]]

sfb = usfb + uusfb
sfb_list = usfb_list + uusfb_list
usfb_list.sort(reverse = True, key = lambda x: x[1])
uusfb_list.sort(reverse = True, key = lambda x: x[1])
sfb_list.sort(reverse = True, key = lambda x: x[1])

fullscissor = infullscissor + outfullscissor
fullscissor_list = infullscissor_list + outfullscissor_list
infullscissor_list.sort(reverse = True, key = lambda x: x[1])
outfullscissor_list.sort(reverse = True, key = lambda x: x[1])
fullscissor_list.sort(reverse = True, key = lambda x: x[1])

halfscissor = inhalfscissor + outhalfscissor
halfscissor_list = inhalfscissor_list + outhalfscissor_list
inhalfscissor_list.sort(reverse = True, key = lambda x: x[1])
outhalfscissor_list.sort(reverse = True, key = lambda x: x[1])
halfscissor_list.sort(reverse = True, key = lambda x: x[1])

roll = inroll + outroll
roll_list = inroll_list + outroll_list
inroll_list.sort(reverse = True, key = lambda x: x[1])
outroll_list.sort(reverse = True, key = lambda x: x[1])
roll_list.sort(reverse = True, key = lambda x: x[1])

print()
prevrow = curr_layout[list(curr_layout.keys())[0]].row
prevfinger = curr_layout[list(curr_layout.keys())[0]].finger
for ltr in curr_layout.keys():
    if curr_layout[ltr].row != prevrow:
        print()
    if curr_layout[ltr].finger - prevfinger > 2:
        print(' ', end = '')
    print(repr(ltr)[1:-1], end = ' ')
    prevrow = curr_layout[ltr].row
    prevfinger = curr_layout[ltr].finger

alt = 0
alt_list = []
inthreeroll = 0
inthreeroll_list = []
outthreeroll = 0
outthreeroll_list = []
oneh = 0
oneh_list = []
altsfs = 0
altsfs_list = []
redsfs = 0
redsfs_list = []
sft = 0
sft_list = []
redirect = 0
redirect_list = []
badredirect = 0
badredirect_list = []

for trigram in data.trigram_freqs.keys():
    if curr_layout[trigram[0]].hand() != curr_layout[trigram[1]].hand() and curr_layout[trigram[1]].hand() != curr_layout[trigram[2]].hand() and (thumbstatsarereal or all(x not in trigram for x in thumb_keys)):
        alt += data.trigram_freqs[trigram]
        alt_list += [[trigram, data.trigram_freqs[trigram]]]
    if curr_layout[trigram[0]].hand() == curr_layout[trigram[1]].hand() == curr_layout[trigram[2]].hand() and (thumbstatsarereal or all(x not in trigram for x in thumb_keys)):
        oneh += data.trigram_freqs[trigram]
        oneh_list += [[trigram, data.trigram_freqs[trigram]]]
        if curr_layout[trigram[0]].finger < curr_layout[trigram[1]].finger < curr_layout[trigram[2]].finger:
            inthreeroll += data.trigram_freqs[trigram]
            inthreeroll_list += [[trigram, data.trigram_freqs[trigram]]]
        elif curr_layout[trigram[0]].finger > curr_layout[trigram[1]].finger > curr_layout[trigram[2]].finger:
            outthreeroll += data.trigram_freqs[trigram]
            outthreeroll_list += [[trigram, data.trigram_freqs[trigram]]]
        elif curr_layout[trigram[0]].finger == curr_layout[trigram[1]].finger == curr_layout[trigram[2]].finger and trigram[0] != trigram[1] and trigram[1] != trigram[2]:
            sft += data.trigram_freqs[trigram]
            sft_list += [[trigram, data.trigram_freqs[trigram]]]
        elif (curr_layout[trigram[0]].finger > curr_layout[trigram[1]].finger) != (curr_layout[trigram[1]].finger > curr_layout[trigram[2]].finger):
            redirect += data.trigram_freqs[trigram]
            redirect_list += [[trigram, data.trigram_freqs[trigram]]]
            fingers_used = [curr_layout[x].finger for x in trigram]
            if 0 in fingers_used or 4 in fingers_used:
                badredirect += data.trigram_freqs[trigram]
                badredirect_list += [[trigram, data.trigram_freqs[trigram]]]
    if curr_layout[trigram[0]].finger == curr_layout[trigram[2]].finger and curr_layout[trigram[0]].finger != curr_layout[trigram[1]].finger and trigram[0] != trigram[2]:
        if curr_layout[trigram[0]].hand() == curr_layout[trigram[1]].hand() == curr_layout[trigram[2]].hand():
            altsfs += data.trigram_freqs[trigram]
            altsfs_list += [[trigram, data.trigram_freqs[trigram]]]
        else:
            redsfs += data.trigram_freqs[trigram]
            redsfs_list += [[trigram, data.trigram_freqs[trigram]]]

threeroll = inthreeroll + outthreeroll
threeroll_list = inthreeroll_list + outthreeroll_list
threeroll_list.sort(reverse = True, key = lambda x: x[1])
inthreeroll_list.sort(reverse = True, key = lambda x: x[1])
outthreeroll_list.sort(reverse = True, key = lambda x: x[1])

sfs = altsfs + redsfs
sfs_list = altsfs_list + redsfs_list
sfs_list.sort(reverse = True, key = lambda x: x[1])
altsfs_list.sort(reverse = True, key = lambda x: x[1])
redsfs_list.sort(reverse = True, key = lambda x: x[1])

oneh_list.sort(reverse = True, key = lambda x: x[1])
sft_list.sort(reverse = True, key = lambda x: x[1])
alt_list.sort(reverse = True, key = lambda x: x[1])
redirect_list.sort(reverse = True, key = lambda x: x[1])
badredirect_list.sort(reverse = True, key = lambda x: x[1])

print(f"""
sfb = {round(sfb * 100, 2)}% (2u: {round(uusfb * 100, 2)}%)
sft = {round(sft * 100, 2)}% 
sfs = {round(sfs * 100, 2)}% (Alt | Red: {round(altsfs * 100, 2)}% | {round(redsfs * 100, 2)}%)
fsb = {round(fullscissor * 100, 2)}% (In | Out: {round(infullscissor * 100, 2)}% | {round(outfullscissor * 100, 2)}%)
hsb = {round(halfscissor * 100, 2)}% (In | Out: {round(inhalfscissor * 100, 2)}% | {round(outhalfscissor * 100, 2)}%)
red = {round(redirect * 100, 2)}% (Bad: {round(badredirect * 100, 2)}%)

alt = {round(alt * 100, 2)}%
rol = {round(roll * 100, 2)}% (In | Out: {round(inroll * 100, 2)}% | {round(outroll * 100, 2)}%)
3rol = {round(threeroll * 100, 2)}% (In | Out: {round(inthreeroll * 100, 2)}% | {round(outthreeroll * 100, 2)}%)
""")

print(threeroll_list)

if verbosity == 1:
    print("Top 10 sfb:")
    for sfb_bigram in sfb_list[slice(10)]:
        print(repr(sfb_bigram[0])[1:-1] + ': ' + str(round(sfb_bigram[1] * 100, 2)) + '%')
    print("\nTop 10 fsb:")
    for fullscissor_bigram in fullscissor_list[slice(10)]:
        print(repr(fullscissor_bigram[0])[1:-1] + ': ' + str(round(fullscissor_bigram[1] * 100, 2)) + '%')
    print("\nTop 10 hsb:")
    for halfscissor_bigram in halfscissor_list[slice(10)]:
        print(repr(halfscissor_bigram[0])[1:-1] + ': ' + str(round(halfscissor_bigram[1] * 100, 2)) + '%')
    print("\nTop 10 roll:")
    for roll_bigram in roll_list[slice(10)]:
        print(repr(roll_bigram[0])[1:-1] + ': ' + str(round(roll_bigram[1] * 100, 2)) + '%')

if verbosity == 2:
    print("sfb:")
    for sfb_bigram in sfb_list:
        print(repr(sfb_bigram[0])[1:-1] + ': ' + str(round(sfb_bigram[1] * 100, 2)) + '%')
    print("2u sfb:")
    for uusfb_bigram in uusfb_list:
        print(repr(uusfb_bigram[0])[1:-1] + ': ' + str(round(uusfb_bigram[1] * 100, 2)) + '%')
    print("\nfsb:")
    for fullscissor_bigram in fullscissor_list:
        print(repr(fullscissor_bigram[0])[1:-1] + ': ' + str(round(fullscissor_bigram[1] * 100, 2)) + '%')
    print("\nhsb:")
    for halfscissor_bigram in halfscissor_list:
        print(repr(halfscissor_bigram[0])[1:-1] + ': ' + str(round(halfscissor_bigram[1] * 100, 2)) + '%')
    print("\nroll:")
    for roll_bigram in roll_list:
        print(repr(roll_bigram[0])[1:-1] + ': ' + str(round(roll_bigram[1] * 100, 2)) + '%')
    print("\ninroll:")
    for inroll_bigram in inroll_list:
        print(repr(inroll_bigram[0])[1:-1] + ': ' + str(round(inroll_bigram[1] * 100, 2)) + '%')
    print("\noutroll:")
    for outroll_bigram in outroll_list:
        print(repr(outroll_bigram[0])[1:-1] + ': ' + str(round(outroll_bigram[1] * 100, 2)) + '%')
