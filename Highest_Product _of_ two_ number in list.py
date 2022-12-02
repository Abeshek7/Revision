import heapq
from operator import mul

list ={7,14,23,-34,-10,57}

output =max(mul(*heapq.nlargest(2,list)),mul(*heapq.nsmallest(2,list)))

print("The Product of the highest Number is :",output)

