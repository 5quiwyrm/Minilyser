corpusname = input("corpus name (without extension): ")

import os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

verbosity = 0

if len(sys.argv) > 1:
    if sys.argv[1] == '1':
        verbosity = 1
    elif sys.argv[1] == '2':
        verbosity = 2

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

nky = 'nokeyishere'

curr_layout = {
    'v' : letter(0, 0), 'l' : letter(0, 1), 'n' : letter(0, 2), 'd' : letter(0, 3), 'k' : letter(0, 3), 'j' : letter(0, 7), 'w' : letter(0, 7), 'o' : letter(0, 6), 'u' : letter(0, 5), ',' : letter(0, 4),
    't' : letter(1, 0), 's' : letter(1, 1), 'r' : letter(1, 2), 'h' : letter(1, 3), 'f' : letter(1, 3), 'g' : letter(1, 7), 'c' : letter(1, 7), 'a' : letter(1, 6), 'e' : letter(1, 5), 'i' : letter(1, 4), '\n' : letter(1, 4),
    'z' : letter(2, 1), 'x' : letter(2, 2), 'p' : letter(2, 3), 'b' : letter(2, 3), '\'' : letter(2, 3), 'm' : letter(2, 7), 'y' : letter(2, 7), 'q' : letter(2, 6), '/' : letter(2, 5), '.' : letter(2, 4),
    ' ' : letter(-2, -2)
}

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
    if curr_layout[bigram[0]].row == curr_layout[bigram[1]].row and bigram[0] != bigram[1] and curr_layout[bigram[0]].finger in [[0, 1, 2, 3], [4, 5, 6, 7], [8]][curr_layout[bigram[1]].finger // 4]:
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

print(f"""
sfb = {round(sfb * 100, 2)}% (2u: {round(uusfb * 100, 2)}%)
fsb = {round(fullscissor * 100, 2)}% (In | Out: {round(infullscissor * 100, 2)}% | {round(outfullscissor * 100, 2)}%)
hsb = {round(halfscissor * 100, 2)}% (In | Out: {round(inhalfscissor * 100, 2)}% | {round(outhalfscissor * 100, 2)}%)
rol = {round(roll * 100, 2)}% (In | Out: {round(inroll * 100, 2)}% | {round(outroll * 100, 2)}%)
""")

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
