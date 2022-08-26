# print the frequency of every item in a list
# using dictionaries
def frequency_dicts(l):
    d = {}
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d.items()

print(frequency_dicts([1,2,2,3]))
# using nested loop

def frequency_loop(l):
    seen, count = [], []

    for i in range(len(l)):
        cnt = 0
        item = l[i]
        if item not in seen:
            for j in l:
                if item == j:
                    cnt += 1
            seen.append(item)
            count.append(cnt)

    for i in range(len(seen)):
        print(seen[i], 'occurs', count[i], 'times')

print(frequency_loop([1,1,2]))

# modified version of above code

def frequency(l):
    res = [0] * (max(l) + 1)

    for i in l:
        res[i] += 1

    for i in range(len(res)):
        if res[i] == 0:
            continue
        print(i, 'occurs', res[i], 'times')

print(frequency([1,1,2,2]))

