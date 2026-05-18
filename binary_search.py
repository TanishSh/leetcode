li = [1, 2, 3, 4, 5]
target = 2

# implement binary search
def bs(li, target):
    # base case
    # get the middle index
    m = (len(li))//2
    # get the middle value (val)
    val = li[m]

    if val == target:
        return m
    
    if val < target:
        return bs(li[m+1::], target)
    elif val > target:
        return bs(li[:m:], target)

print(bs(li, target))


