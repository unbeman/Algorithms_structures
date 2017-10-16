import sys
class Heap:
	def __init__(self, array=[]):
		self.__array = array
		self.__size = len(array) 
		if array:
			for i in range(self.__size // 2, -1, -1):
				self.__sift_down(i)

	def __str__(self):
		return str(self.__array)
		
	def __parent(self, i):
		return (i - 1) // 2

	def __left_child(self, i):
		return 2 * i + 1

	def __right_child(self, i):
		return 2 * i + 2


	def __sift_up(self, i):
		p = self.__parent(i)
		while i > 0 and self.__array[p] < self.__array[i]:
			self.__array[p], self.__array[i] = self.__array[i], self.__array[p]
			i = p
			p = self.__parent(i)
	
	def __sift_down(self, i):
		maxi = i
		l = self.__left_child(i)
		size = self.__size
		if l < size and self.__array[l] > self.__array[maxi]:
			maxi = l
		r = self.__right_child(i)
		if 	r < size and self.__array[r] > self.__array[maxi]:
			maxi = r
		if maxi != i:
			self.__array[i], self.__array[maxi] = self.__array[maxi], self.__array[i]
			self.__sift_down(maxi)

	def Insert(self, p):
		self.__array.append(p)
		self.__size += 1
		self.__sift_up(self.__size - 1)
	
	def ExtractMax(self):
		res = self.__array[0]
		self.__array[0] = self.__array[self.__size - 1]
		self.__sift_down(0)
		self.__size -= 1
		self.__array.pop()
		return res

	def Remove(self, i):
		self.__array[i] = sys.maxsize
		self.__sift_up(i)
		self.ExtractMax()

	def GetMax(self):
		return self.__array[0]


	def ChangePriority(self, i, p):
		old = self.__array[i]
		self.__array[i] = p
		if p > old:
			self.__sift_up(i)
		else:
			self.__sift_down(i)		

	def GetArray(self):
		return list([i for i in self.__array])			

	def HeapSort(self):
		size = self.__size
		for i in range(size):
			self.__array[0], self.__array[self.__size - 1] = self.__array[self.__size - 1], self.__array[0]
			self.__size -= 1
			self.__sift_down(0)
		self.__size = size
		self.__array.reverse()
		return self.GetArray()		

a = [1, 2, 3, 4, 5]
N = Heap(a)
print(N)
a = N.HeapSort()
print(a)
