def isPalindrome(s):
	i=0
	j=len(s)-1
	while i < j and s[i]==s[j]:
		i=i+1
		j=j-1
	return j<=i

s1=raw_input("Enter a string ")
print(s1 + " is a palindrome ? " + str(isPalindrome(s1)))
