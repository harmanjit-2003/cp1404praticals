# Part a: Count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Part b: Count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Part c: Print n stars based on user input
n = int(input("Number of stars: "))
for _ in range(n):
    print('*', end='')
print()

# Part d: Print n lines of increasing stars
n = int(input("Number of lines: "))
for i in range(1, n + 1):
    print('*' * i)
