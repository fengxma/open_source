def lonelyinteger(b):
    b = list(b)
    total_range = range(len(b))
    records = [0] * len(b)

    if len(b) == 1:
        return b[0]
    else:
        for i in total_range[:-1]:
            for j in total_range[(i+1):]:
                if b[j] == b[i]:
                    records[i] = records[j] = 1
                    print(records)
        for i in total_range:
            if records[i] == 0:
                return b[i]
    print(records)

# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = map(int, input().strip().split(" "))
    print(lonelyinteger(b))