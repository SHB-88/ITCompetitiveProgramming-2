def sumSquare( n) :
	i = 1
	while i * i <= n :
		j = 1
		while(j * j <= n) :
			if (i * i + j * j == n) :
				print(i, "^2 + ", j , "^2" )
				return True
			j = j + 1
		i = i + 1
		
	return False

n = 25
if (sumSquare(n)) :
	print("Yes")
else :
	print( "No")
	
