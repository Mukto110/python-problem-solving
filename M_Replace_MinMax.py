n = input()
a = input().split()
for i in range(len(a)):  
    a[i] = int(a[i])

min_index = a.index(min(a))
max_index = a.index(max(a))

a[min_index], a[max_index] = a[max_index], a[min_index]

print(*a)    