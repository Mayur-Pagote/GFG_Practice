	def isSame(self, s):
		# code here
		char = 0
		num = ""
		for i in s:
		    if i.isalpha():
		        char += 1
		    else:
		        num += i
		if char == int(num):
		    return 1
		else:
		    return 0
