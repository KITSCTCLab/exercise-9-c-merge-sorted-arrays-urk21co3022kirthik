from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  # Write code here
  position = len(nums1) - n
  while position < len(nums1):
    nums1[position] = 0
    position += 1
  last= m+n-1
  while m>0 and n>0:
      if nums1[m-1]>nums2[n-1]:
          nums1[last]=nums1[m-1]
          m -=1
      else:
          nums1[last]=nums2[n-1]
          n-=1
      last-=1
  while n>0:
      nums1[last]=nums2[n-1]
      n,last=n-1,last-1


# Do not change the following code
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
