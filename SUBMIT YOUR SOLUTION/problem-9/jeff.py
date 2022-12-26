
def interSection(arr1,arr2):
    
	result = list(filter(lambda x: x in arr1, arr2))
	print ("Intersection : ",result)
	
if __name__ == "__main__":
    
	arr1 = [-9,1,2,3,4,0,-2]
	arr2 = [2,8,-1,4]
	interSection(arr1,arr2)
