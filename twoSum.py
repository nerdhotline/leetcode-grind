'''
INTUITION:

for this example, let lst=[2, 7, 11, 15]


So, the way I was thinking about this was to search for the complement 
of the current number we're on, using a hash table to store the difference
of the target and the current list element. So on our first iteration, we'd
*-----------------------* be looking for 2's complement, which is 7. 
|                       | 
| +----+----+----+----+ | The problem with this set up is that the hash table
| |  2 |  7 | 11 | 15 | | isn't saving us time, as the subtraction is already
| +----+----+----+----+ | a constant operation. We want to use the hash table
|    ^                  | more effectively! Additionally, this setup also runs
*-----------------------* into the problem that you can return [i, i]. The ket
to efficiently solving this guy is to think about it in reverse. 

Let's make our hash table store the list element as the key, and its index as 
the value to make grabbing this part of the answer constant. Then, as we traverse 
we ask "Have I seen lst[i]'s complement yet?" If we have, then we're done! Otherwise, 
we add this number to the dictionary.

Python Tip: if you need to access the index and its value, enumerate is WAY faster.
'''

def twoSum(self, nums: list[int], target: int) -> list[int]:
  numsDict = {}
  
  for indx, val in enumerate(nums):
    complement = target - val

    if (complement in numsDict):
        return [numsDict[complement], indx]
    numsDict[val] = indx 