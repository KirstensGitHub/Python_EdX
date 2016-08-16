def exactChange(amount, coinList):
	if amount ==0;
		return True
	if coinList ==[]:
		return False
	#^base cases

	useIt=exactChange(amount-coinList[0], coinList[1:])
	loseIt=exactChange(amount, coinList[1:])

	return useIt or loseIt

