import random as rdm
import timeit

## N = int(1e5)
## M = [rdm.random()**2+rdm.random()**2 <= 1 for _ in range(N)]
#M=0
#for _ in range(N):
#    x = rdm.random()
#    y = rdm.random()
#    M += x**2+y**2 <=1
  #  if r <= 1:
  #      M += 1 
  #  else:
  #      continue
# pi = 4*M/N
a=timeit.timeit(setup= '''
import random as rdm
import timeit
N = int(1e5)
''', stmt= '''
M = [rdm.random()**2+rdm.random()**2 <= 1 for _ in range(N)]
''', number = 1000)

b= timeit.timeit(setup= '''
import random as rdm
import timeit

N = int(1e5)''', stmt= '''
m=0
for _ in range(N):
    x = rdm.random()
    y = rdm.random()
    if x**2+y**2 <= 1:
       m += 1 
    else:
       continue''', number=1000)

#print("pigreco viene:", 4*sum(M)/N)
print("tempo metodo efficiente =", a)
print("tempo metodo inefficiente =", b)



