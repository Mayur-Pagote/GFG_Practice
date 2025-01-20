class Solution:
	def removeCharacters(self, s):
		# code here
		S = ""
		for i in s:
		    if i.isdigit():
		        S += i
		return S
