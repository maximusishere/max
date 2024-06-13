# a = input().rstrip()

a = '6 5 4 8'
data = list(map(int, a.split()))


def find_smaller_number(data):
    quantity = []
    for m in range(len(data)):
        num = 0

        for i in data:
            # numb = data[i]
            if i < data[m]:
                num +=1
        quantity.append(num)

    return quantity

print(find_smaller_number(data))
