def solution(x,y):
	prisonerID=1
	for i in range(1,x):
	    prisonerID+=(i+1)
	for j in range(1,y):
	    prisonerID+=x
	    x+=1
	return prisonerID