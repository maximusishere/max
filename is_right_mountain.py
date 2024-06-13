x = '2 4 5 4 3'
num22 = [int(x) for x in x.split()]

def is_right_mountain(num22):
    left = right = 0
    for i in range(len(num22)-1):
        if num22[i] < num22[i+1]:
            if right:
                return False
            left += 1
        elif num22[i] > num22[i+1]:
            if not left:
                return False
            right += 1
        else:
            return False
    return bool(left and right)
 
#*arr, = map(int, input('->').split())
print(is_right_mountain(num22))