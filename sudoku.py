#/usr/bin/env python
subject=[
[1,5,0,0,0,4,0,9,7],
[0,8,0,1,3,0,0,0,2],
[0,0,9,0,0,6,8,0,0],
[3,0,8,0,4,0,0,6,0],
[0,4,0,0,0,8,0,1,0],
[0,6,0,0,1,7,4,0,9],
[0,0,2,4,0,0,3,0,0],
[8,0,0,0,9,3,0,5,0],
[6,3,0,7,0,0,0,2,4]]

subject = [
[0,0,7,0,0,0,9,0,0],
[4,0,0,0,8,0,5,7,0],
[9,0,0,2,0,1,0,0,6],
[0,0,0,4,6,0,0,0,0],
[5,0,6,0,0,0,8,0,2],
[0,0,0,0,1,5,0,0,0],
[3,0,0,7,0,4,0,0,8],
[0,1,4,0,5,0,0,0,9],
[0,0,9,0,0,0,7,0,0]]

subject = [
[0,5,0,0,7,8,0,0,0],
[0,0,0,0,0,0,0,3,5],
[0,0,0,6,0,0,0,8,4],
[4,0,5,0,0,2,0,9,0],
[0,0,0,0,0,0,0,0,0],
[0,2,0,7,0,0,1,0,6],
[9,3,0,0,0,5,0,0,0],
[8,4,0,0,0,0,0,0,0],
[0,0,0,1,9,0,0,2,0]]

# is the position already given a fixed number
fixed=[]
for row in subject:
	fixed += [bool(item) for item in row]

# 0~80
def getitem1x(pos1x):
	return subject[pos1x/9][pos1x%9]

# (0,0)~(8,8)
def getitem2x(pos2x):
	return subject[pos2x[0]][pos2x[1]]

# candidate numbers for current position
def findnum(pos2x):
	candi = range(getitem2x(pos2x)+1, 10)
	row = subject[pos2x[0]]
	col = [subject[i][pos2x[1]] for i in range(0, 9)]
	grid_top = pos2x[0]/3*3
	grid_left = pos2x[1]/3*3
	grid = []
	for i in range(0, 3):
		for j in range(0, 3):
			grid.append(subject[grid_top+i][grid_left+j])
	ret = []
	for item in candi:
		if not ((item in row) or (item in col) or (item in grid)):
			ret.append(item)
	return ret

back = False # backtrace flag
pos1x = 0
while pos1x >= 0 and pos1x < len(fixed):
	if fixed[pos1x]:
		if back:
			pos1x -= 1
		else:
			pos1x += 1
	else:
		pos2x = [pos1x/9, pos1x%9]
		candi = findnum(pos2x)
		#print pos2x, ' -> ', candi
		if candi:
			subject[pos2x[0]][pos2x[1]] = candi[0]
			pos1x += 1
			back = False
		else:
			subject[pos2x[0]][pos2x[1]] = 0
			pos1x -= 1
			back = True

if pos1x == len(fixed):
	for row in subject:
		print row
else:
	print 'cannot find a solution'
