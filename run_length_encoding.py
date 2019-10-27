def rle(data):
    count = 1
    ans = []
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            ans.append((count, data[i - 1]))
            count = 1
    else:
        ans.append((count, data[i]))
    return ans

