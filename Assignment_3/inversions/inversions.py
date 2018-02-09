#python3
import sys

def f(aL):
	global count
	count = 0
	def MergeSort(aList):
		global count
		if len(aList)>1:
			mid = len(aList)//2
			left = aList[:mid]
			right = aList[mid:]

			MergeSort(left)
			MergeSort(right)

			i,j,k = 0,0,0

			while i < len(left) and j < len(right):
				if left[i] <= right[j]:
					aList[k] = left[i]
					i += 1
				else:
					count += len(left)-i
					aList[k] = right[j]
					j += 1
				k += 1
			while i < len(left):
				aList[k] = left[i]
				i,k = i+1, k+1
			while j < len(right):
				aList[k] = right[j]
				j,k = j+1, k+1
		#print(aList)
	MergeSort(aL)
	return count
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(f(a))
