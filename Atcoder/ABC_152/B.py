a, b = list(map(int,input().split()))

A = str(a)*b
B = str(b)*a

array = [A,B]
array.sort()

print(array[0])