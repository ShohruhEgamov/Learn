def ketma(end, start):
	if start > end:
		return
	print(start)
	ketma(end,start + 1)
ketma(100, 20)
