# TASK1 
# WHILE LOOP

n = int(input("Enter a number: "))
i = 1
total = 0
while i <= n:
    print(i)
    total += i
    i += 1
print("sum:", total)


# TASK2
# FOR LOOP with RANGE

print(" Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

    print("\nEven numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i)

    print("\nNumbers from 20 to 1:")
for i in range(20, 0, -1):
        print(i)


# TASK3
# BREAK ANDCONTINUE 

# USING BREAK
print("Using break:")
for i in range(1, 16):
    if i == 8:
        break
    print(i)

# USING CONTINUE
print("Using continue:")
for i in range(1, 16):
    if i % 3 == 0:
        continue
    print(i)
    

# TASK4
# NESTED LOOP PATTERN

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
