def binary(arr,x):
  st=0
  l=len(arr)
  mid=0
  while(st<=l):
      mid=(st+l)//2
      if(x>arr[mid]):
          st=mid+1
      elif(x<arr[mid]):
          l=mid-1
      else:
          return mid
  return -1
arr=[2,3,4,10,5]
x=10
result=binary(arr,x)
if result !=-1:
    print(result)
else:
    print('not found')
  // check indent
