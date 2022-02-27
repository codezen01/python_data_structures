Dynamic Programming¶
Many programs in computer science are written to optimize some value; 
for example, find the shortest path between two points, find the line that best fits a set of points, or find the smallest set of objects that satisfies some criteria.
There are many strategies that computer scientists use to solve these problems. One of the goals of this book is to expose you to several different problem solving strategies. 
Dynamic programming is one strategy for these types of optimization problems.


def recDC(coinValueList,change,knownResults):
   minCoins = change
   if change in coinValueList:
      knownResults[change] = 1
      return 1
   elif knownResults[change] > 0:
      return knownResults[change]
   else:
       for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recDC(coinValueList, change-i,
                              knownResults)
         if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
   return minCoins

print(recDC([1,5,10,25],63,[0]*64))
