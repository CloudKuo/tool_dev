class for_bubble(object):
    def bubbleSort(self, items):
        def swap(firstIndex, secondIndex):
            temp = items[firstIndex]
            items[firstIndex] = items[secondIndex]
            items[secondIndex] = temp

        length = len(items)

        for i in range(length):
            j = 0
            stop = length - i
            while j < stop - 1:
                if items[j] > items[j + 1]:
                    swap(j, j + 1)
                j += 1
        return items
a = [1,4,2,5,6,7]
b = for_bubble()
print(b.bubbleSort(a))

