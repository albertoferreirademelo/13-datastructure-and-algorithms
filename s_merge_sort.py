class sortering:

    def merge(self,left, right):   
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1       
        result += left[i:]    
        result += right[j:]    
        return result
    
    
    def mergesort(self, listan):    
        if len(listan) <= 1:
            return listan
        middle = int(len(listan) / 2)
        left = self.mergesort(listan[:middle])    
        right = self.mergesort(listan[middle:])    
        return self.merge(left, right)
    
    
import random
import time

listan = []
for i in range(10000):
    listan.append(random.randrange(100))


print (listan)
start_time = time.clock()
print (sortering.mergesort(listan))
print (time.clock() - start_time, "seconds")