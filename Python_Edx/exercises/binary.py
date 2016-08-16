
def isOdd(n):
	"""
	determines if number is odd 
	input: int
	output: boolean (True/False)
	"""
	if n%2 == 0:
		return False
	else:
		return True

def numToBinary(N):
    """
    inputs: float
    output: binary
    """
    binary=[]
    while N>0:
        if isOdd(N):
            binary.append(1)
            N=N-1
        if not isOdd(N):
            binary.append(0)
            N=N/2
    if N==0:
        binary.append(0)
        
    return binary[::-1]


  
def binToNum():
    """ 
    	input: binary
    	output: int
    """
    return random.choice([-1,1])