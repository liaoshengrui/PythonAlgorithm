# coding:utf-8

# 冒泡排序
def bubble_sort(list):
    # 外圈循环缩小
    n = len(list)
    for i in range(len(list) - 1):
        count = 0
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
        if count == 0:
            return


# 插入排序
def insertion_sort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[i], list[j] = list[j], list[i]


# 选择排序
def selection_sort(list):
    size = len(list)
    for i in range(size - 1):
        min = i
        for j in range(i + 1, size):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[i], list[min] = list[min], list[i]


# 快速排序
def quick_sort(list, frist, last):
    if frist >= last:
        return

    mid_value = list[frist]
    low = frist
    high = last

    while low < high:

        while low < high and list[high] >= mid_value:
            high -= 1

        list[low] = list[high]

        while low < high and list[low] < mid_value:
            low += 1

        list[high] = list[low]

    list[low]=mid_value
    quick_sort(list, frist, last-1)
    quick_sort(list, frist+1, last)


# 希尔排序
def shell_sort(list):
    size = len(list)
    gap = size // 2

    while gap > 0:
        for j in range(gap, size):
            i = j
            while i > 0:
                if list[i] < list[i - gap]:
                    list[i], list[i - gap] = list[i - gap], list[i]
                    i -= gap
                else:
                    break
        gap //= 2


def main():
    list = [8, 3, 6, 4, 9, 5, 9]
    bubble_sort(list)
    print(list)

    list = [8, 3, 6, 4, 9, 5, 9]
    quick_sort(list, 0, len(list) - 1)
    print(list)


if __name__ == '__main__':
    main()
