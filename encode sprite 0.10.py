from PIL import Image
import numpy as np


#change short_line length (0->1), (1->2), ... , (15->16)

""" calc hex
>>> int('a',16)
10
>>> hex(int('a',16) + 1)
'0xb'
"""
def encode_line(line, ypos, palette):#in-> line_pos ,out-> line_arr
    out_first = list("0x00") # N_lines, start_pos
    out_arr = []
    x_pos = 0

    while (x_pos <= 15):
        short_line = list("0x00") #color, length(0 represents length 1, 1 is 2, ... , 15 is 16)
        out = False
        short_line[2] =  str(palette.index(line[x_pos]))
        x_pos+=1
        
        while (out == False and x_pos <=15):
            if int(short_line[2]) != palette.index(list(line[x_pos])):
                break
            short_line[3] =  hex(int(short_line[3],16)+1)[2]
            #print(short_line)
            x_pos+=1
            
        out_arr.append(short_line)
        
    ################
    if out_arr[-1][2] == '0':
        del out_arr[-1]
    if out_arr[0][2] == '0' and len(out_arr) != 0:
        out_first[3] = out_arr[0][3]
        del out_arr[0]

    
    out_first[2] = str(len(out_arr))
    out_arr = [''.join(i) for i in out_arr]
    out_arr = [''.join(out_first)] + out_arr
    return out_arr



####################################################################################
####################################################################################
####################################################################################



DECODE_DIR = "IMAGE DIRECTORY HERE"
palette = [[255,255,255], # PUT PALETTE HERE #
           [32,32,32],
           [48,48,48],
           [64,64,64]]

img = Image.open(DECODE_DIR)
img = np.array(img) #[y, x, color]
y_pos = 0

#print(list(img[0][1])[2], type(list(img[0][1])))
for i in range(16):
    line = [list(j) for j in img[i]]
    print(", ".join(encode_line(list(line),i,palette)))




