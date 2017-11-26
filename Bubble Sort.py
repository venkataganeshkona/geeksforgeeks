#Worst Case O(n^2) and Average Case O(n^2)

N = input()
A = raw_input()
array = map(int, A.split())
# rint array
N = len(array)
count = 0
temp = 0
if N == 0:
    print count
elif N == 1:
    print count + 1
elif N > 1:
    for i in range(0, N - 1):
        for j in range(0, N - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                count = count + 1

print count