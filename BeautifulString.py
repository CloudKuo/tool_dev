

def isBeautifulString(inputString):
    a = sorted(list(inputString))
    all_count_list = []
    count = 0
    for i in range(len(a)):
        if i == 0:
            first = a.count(a[i])
            all_count_list.append(first)
        elif a[i] != a[i-1]:
            diff = a.count(a[i])
            all_count_list.append(diff)
        elif i == len(a)-1 and a[i] != a[i-1]:
            last = a.count(a[i])
            all_count_list.append(last)
    print(all_count_list)

    if max(all_count_list) == all_count_list[0]:
        return True
    else:
        return False

print(isBeautifulString('aaaffffbbbcc'))