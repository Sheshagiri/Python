def isPalindrome(s):
	i=0
	j=len(s)-1
	while i < j and s[i]==s[j]:
		i=i+1
		j=j-1
	return j<=i

print(isPalindrome('racecar'))
