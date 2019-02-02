result = []
for i in range(100, 500):
        item = []
        for num in str(i):
            if int(num) % 2 == 1:
                item.append(num)
            else:
                item = []
                break
        if item:
            result.append("".join(item))
print(",".join(result))


