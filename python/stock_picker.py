import itertools

def picker(prices):
    arr =[[0]]
    count = 0

    for idx1, value1 in enumerate(prices):
        for idx2 in range(1, len(prices), 1):
            # print(idx2)
            if value1 < prices[idx2]:

                if prices[idx2] - value1 > count and idx1 < idx2:                    
                    count = prices[idx2] - value1
                    # print(arr)
                    arr.pop(0)
                    # print(arr)
                    arr.append([idx1, idx2])
                    # print(arr)
            else:
                continue 
    return list(itertools.chain(*arr))
