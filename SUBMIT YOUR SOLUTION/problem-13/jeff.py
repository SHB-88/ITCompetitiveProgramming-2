NO_OF_CHARS = 256

def areAnagram(str1,str2):
	if(len(str1) != len(str2)):
		return False;

	count=[0 for i in range(NO_OF_CHARS)]
	i=0
	
	for i in range(len(str1)):
		count[ord(str1[i]) - ord('a')] += 1;
		count[ord(str2[i]) - ord('a')] -= 1;
		
	for i in range(NO_OF_CHARS):
		if (count[i] != 0):
			return False
	return True

str1="silent"
str2="listen"

if (areAnagram(str1, str2)):
	print("TRUE")
else:
	print("FALSE")

