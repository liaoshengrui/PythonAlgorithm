# coding:utf-8

# 冒泡排序
def a_sort(list):
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
def b_sort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[i], list[j] = list[j], list[i]


# 选择排序
def c_sort(list):
    size = len(list)
    for i in range(size - 1):
        min = i
        for j in range(i + 1, size):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[i], list[min] = list[min], list[i]


# 快速排序
def d_sort(list):
    pass


def main():
    list = [8, 3, 6, 4, 9, 5, 9]
    list2 = [8, 3, 6, 4, 9, 5, 9]
    a_sort(list)
    c_sort(list2)
    print(list)
    print(list2)


if __name__ == '__main__':
    main()
