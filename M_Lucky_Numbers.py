a, b = input().split()
a = int(a)
b = int(b)

lucky_numbers = []

for num in range(a, b + 1):
    if all(digit in "47" for digit in str(num)):
        lucky_numbers.append(num) 


if lucky_numbers:
    print(*lucky_numbers) 
else:
    print(-1)       