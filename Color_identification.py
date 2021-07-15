# Importing the required packages

import cv2
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Assigning the image path and CSV path to respective variables

img_path = 'Holi.jpg'
csv_path = 'colours.csv'

# Reading CSV file

index = ['Color', 'Color name', 'Hex', 'R', 'G', 'B']
identifyColor = pd.read_csv(csv_path, names = index)

# Reading the image using imread()

img = cv2.imread(img_path)
img = cv2.resize(img, (800,600))
clicked = False
r = g = b = xpos = ypos = 0

# A function to get the most suitable color by calculationg the minimum distance

def get_color_name(R,G,B):
	minimum = 1000
	for i in range(len(identifyColor)):
		distance = abs(R - int(identifyColor.loc[i,'R'])) + abs(G - int(identifyColor.loc[i,'G'])) + abs(B - int(identifyColor.loc[i,'B']))
		if distance <= minimum:
			minimum = distance
			color_name = identifyColor.loc[i, 'Color name']

	return color_name

# A function to get x,y coordinates with double click of mouse
# Initialzing global variables

def mouseClick(event, x, y, flags, param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y
		b,g,r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)

# To create a window

cv2.namedWindow('Image')
cv2.setMouseCallback('Image', mouseClick)


# To display name of the colours and RGB values

while True:
	cv2.imshow('Image', img)
	if clicked:

		cv2.rectangle(img, (30,30), (600,60), (b,g,r), -1)

		text = get_color_name(r,g,b) + ' R= ' + str(r) + ' G= ' + str(g) + ' B= ' + str(b)
		
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255), 2, cv2.LINE_AA)

		# Displaying Text in black for light colors
		if r+g+b >= 400:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0), 2, cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()