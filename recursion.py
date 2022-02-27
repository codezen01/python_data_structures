Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. 
Usually recursion involves a function calling itself. 
While it may not seem like much on the surface, recursion allows us to write elegant solutions to problems that may otherwise be very difficult to program.

Like the robots of Asimov, all recursive algorithms must obey three important laws:

A recursive algorithm must have a base case.
A recursive algorithm must change its state and move toward the base case.
A recursive algorithm must call itself, recursively.

ActiveCode 1 shows the Python code that implements the algorithm outlined above for any base between 2 and 16.

def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16)
      

 ===========================
    
      
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
      
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)
      
      
      ====================================
