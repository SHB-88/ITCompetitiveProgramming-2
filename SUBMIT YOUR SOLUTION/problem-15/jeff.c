
#include <stdio.h>

int cr(int arr[], int n)
{
	int min = arr[0], min_index = 0;
	for (int i = 0; i < n; i++) {
		if (min > arr[i]) {
			min = arr[i];
			min_index = i;
		}
	}
	return min_index;
}
int main()
{
	int arr[] = { 8, 9, 10, 2, 5, 6 };
	int n = sizeof(arr) / sizeof(arr[0]);
	printf("total number of times the array is rotated to be sorted is : %d", cr(arr, n));
	return 0;
}

