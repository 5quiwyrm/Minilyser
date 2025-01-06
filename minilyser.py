corpusname = input("corpus name (without extension): ")

try:
    exec(f"import {corpusname}data as data")
except:
    raise Exception(f"The data for {corpusname} has not been generated yet, refer to README for information on how to generate data.")
print(f"{corpusname} loaded as corpora of choice")

class letter:
    def __init__(self, row, finger):
        self.row = row
        self.finger = finger

nky = 'nokeyishere'

curr_layout = {
    {'v' : letter(0, 0)}, {'l' : letter(0, 1)}, {'n' : letter(0, 2)}, {'d' : letter(0, 3)}, {'k' : letter(0, 3)}, {'j' : letter(0, 7)}, {'w' : letter(0, 7)}, {'o' : letter(0, 6)}, {'u' : letter(0, 5)}, {',' : letter(0, 4)},
    {'t' : letter(1, 0)}, {'s' : letter(1, 1)}, {'r' : letter(1, 2)}, {'h' : letter(1, 3)}, {'f' : letter(1, 3)}, {'g' : letter(1, 7)}, {'c' : letter(1, 7)}, {'a' : letter(1, 6)}, {'e' : letter(1, 5)}, {'i' : letter(1, 4)},
    {'z' : letter(2, 1)}, {'x' : letter(2, 2)}, {'p' : letter(2, 3)}, {'b' : letter(2, 3)}, {'\'' : letter(2, 3)}, {'m' : letter(2, 7)}, {'y' : letter(2, 7)}, {'q' : letter(2, 6)}, {'/' : letter(2, 5)}, {'.' : letter(2, 4)},
    {' ' : letter(-2, -2)}
}

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
        if curr_layout[bigram[0]] > curr_layout[bigram[1]]:
            infullscissor += data.bigram_freqs[bigram]
            infullscissor_list += [[bigram, data.bigram_freqs[bigram]]]
        else:
            outfullscissor += data.bigram_freqs[bigram]
            outfullscissor_list += [[bigram, data.bigram_freqs[bigram]]]
    if abs(curr_layout[bigram[0]].row - curr_layout[bigram[1]].row) == 1 and abs(curr_layout[bigram[0]].finger - curr_layout[bigram[1]].finger) == 1:
        if curr_layout[bigram[0]] > curr_layout[bigram[1]]:
            inhalfscissor += data.bigram_freqs[bigram]
            inhalfscissor_list += [[bigram, data.bigram_freqs[bigram]]]
        else:
            outhalfscissor += data.bigram_freqs[bigram]
            outhalfscissor_list += [[bigram, data.bigram_freqs[bigram]]]
    if curr_layout[bigram[0]].row == curr_layout[bigram[1]].row and bigram[0] != bigram[1]:
        if curr_layout[bigram[0]] > curr_layout[bigram[1]]:
            inroll += data.bigram_freqs[bigram]
            inroll_list += [[bigram, data.bigram_freqs[bigram]]]
        else:
            outroll += data.bigram_freqs[bigram]
            outroll_list += [[bigram, data.bigram_freqs[bigram]]]

sfb = usfb + uusfb
sfb_list = usfb_list + uusfb_list
usfb_list.sort(reverse = True)
uusfb_list.sort(reverse = True)
sfb_list.sort(reverse = True)

fullscissor = infullscissor + outfullscissor
fullscissor_list = infullscissor_list + outfullscissor_list
infullscissor_list.sort(reverse = True)
outfullscissor_list.sort(reverse = True)
fullscissor_list.sort(reverse = True)

halfscissor = inhalfscissor + outhalfscissor
halfscissor_list = inhalfscissor_list + outhalfscissor_list
inhalfscissor_list.sort(reverse = True)
outhalfscissor_list.sort(reverse = True)
halfscissor_list.sort(reverse = True)

roll = inroll + outroll
roll_list = inroll_list + outroll_list
inroll_list.sort(reverse = True)
outroll_list.sort(reverse = True)
roll_list.sort(reverse = True)
