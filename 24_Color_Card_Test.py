# ************************************
# *                                  *
# *                                  *
# *  24 COLOR CARD TEST              *
# *                                  *
# *                                  *
# *  Date       : 2018.12.15         *
# *  Version    : 1.0.0              *     
# *  Written by : nagypup@gmail.com  *
# *                                  * 
# *                                  *
# ************************************

from tkinter import *

# Input_Ration : setup a magnification according to the desktop resolution
Input_Ratio=1

# initialize tkinter
my_window = Tk()
my_window.title("24 Color Card Test")
my_window.resizable(width=False, height=False)

# data set of showed tiles by R-G-B order
my_list = [
[115,82,69],
[204,161,141],
[101,134,179],
[89,109,61],
[141,137,194],
[132,228,208],
[249,118,35],
[80,91,182],
[222,91,125],
[91,63,123],
[173,232,91],
[255,164,26],
[44,56,142],
[74,148,81],
[179,42,50],
[250,226,21],
[191,81,160],
[6,142,162],
[252,252,252],
[230,230,230],
[200,200,200],
[143,143,142],
[100,100,100],
[50,50,50]]

# main cycles
for j in range(0,4):
    for i in range(0,6):
        l = j*6+i
        str='#'
        for k in range(0,3):
            str = str + hex(my_list[l][k]).split('x')[-1].zfill(2)
        my_canvas = Canvas(my_window, width = Input_Ratio*100, height=Input_Ratio*100, background=str)
        my_canvas.grid(row=j, column=i)

# main loop
my_window.mainloop()
