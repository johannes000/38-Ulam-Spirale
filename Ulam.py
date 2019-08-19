import sieb
import scipy.misc
from PIL import Image
import numpy as np


dimension = 500
newpos = 0,0
grid = [[0 for x in range(dimension)] for y in range(dimension)] 
primzahlen = sieb.gen_prime_list(dimension*dimension)

def __genImage(grid):
	img = np.zeros((dimension,dimension,3),dtype=np.uint8)
	for y in range(0,len(grid)):
		for x in range (0,len(grid[0])):
			if grid[y][x] in primzahlen:
				img[y][x][0] = 0
				img[y][x][1] = 0
				img[y][x][2] = 0
			else:
				img[y][x][0] = 100
				img[y][x][1] = 100
				img[y][x][2] = 100	
	img = scipy.misc.imresize(img, (5000, 5000))
	scipy.misc.imsave("image.png", img)




def __feldAnzeigen(grid,primzahlen):
	for spalte in range(0,len(grid)):
		for zeile in range (0,len(grid[0])):
			if grid[spalte][zeile] in primzahlen:
				print ("!",grid[spalte][zeile],end="" )
			else:
				print (" ",grid[spalte][zeile],end="" )
		print("")

def __feldAnzeigenPunkte(grid,primzahlen):
	for spalte in range(0,len(grid)):
		for zeile in range (0,len(grid[0])):
			if grid[spalte][zeile] in primzahlen:
				print ("O",end="" )
			else:
				print ("X",end="" )
		print("")

def __isFree(grid,x,y):
	if x >= dimension or x< 0 or y >= dimension or y< 0:
		return True		
	return grid[x][y] != 0


def __gen_spirale(grid):
	pos = 0,dimension-1
	nachbarn = [[0,0],[0 ,-1],[1 , 0],[0 ,1],[-1 , 0]]
	i=0
	for n in reversed(range(1,(dimension*dimension)+1)):		
		richtung = nachbarn[i]
		if not __isFree(grid,pos[0]+richtung[0],pos[1]+richtung[1]):
			grid[pos[0]+richtung[0]][pos[1]+richtung[1]] = n
			pos=pos[0]+richtung[0],pos[1]+richtung[1]
		if __isFree(grid,pos[0]+richtung[0],pos[1]+richtung[1]):
			i = i+ 1
			if i > 4:
				i = 1

__gen_spirale(grid)
__genImage(grid,primzahlen)

#__feldAnzeigenPunkte(grid,primzahlen)
