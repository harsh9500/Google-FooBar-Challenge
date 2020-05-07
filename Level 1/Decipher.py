def solution(x):
	decodedString=""
	toSubtractFrom=ord('z')+ord('a')
	for i in x:
	    if i.islower():
	    	print i
	        currVal=ord(i)
	        print currVal
	        decodedString+=chr(toSubtractFrom-currVal)
	    else:
	        decodedString+=i
	return decodedString