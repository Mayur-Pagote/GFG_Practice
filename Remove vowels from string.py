class Solution:
	def removeVowels(self, s):
		# code here
		l = ["a", "e", "i", "o", "u"]
		S = ""
		for i in s:
		    if i in l:
		        continue
		    else:
		        S += i
		return S
