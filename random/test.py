count1 = 0
n = 4

for i in range(n):
    for j in range(n):
        count1 += 1
        print(f"i: {i}, j: {j}, count: {count1}")
        if j == i:
            break