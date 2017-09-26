lists = []

for item in range(4):
    num = int(input("Enter the temp..."))
    lists.append(num)
print(max(lists))

def mean(lists):
    return float(sum(lists)) / max(len(lists), 1)
print(mean(lists))

