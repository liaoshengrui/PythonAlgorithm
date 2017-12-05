# coding:utf-8

def index(tar, prt):
    i = 0
    j = 0
    n = len(tar)
    m = len(prt)

    while i < n and j < m:

        if tar[i] == prt[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j == m:
        return i - m
    else:
        return 0


def index_pro(tar, prt):
    i = 0
    n = len(tar)
    m = len(prt)

    while i < n - m + 1:

        sub = tar[i:m + i]

        if sub == prt:
            return i
        else:
            i += 1

    return 0


# kmp算法
def KMP_index(text, pattern):
    i = 0
    j = 0
    next = get_next(pattern)

    while i < len(text) and j < len(pattern):

        if j==0 or text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            j = next[j]

    if j == len(pattern):
        return i - j
    else:
        return 0


def get_next(pattern):
    size = len(pattern)
    next = [0 for x in range(size)]
    j = 0
    for i in range(1,size):

        while j >0 and pattern[j] != pattern[i]:
            j=next[j-1]

        if pattern[i] == pattern[j]:
            j+=1
            next[i]=j

    return next


def main():
    text = "abcdabd"
    pattern = "cd"

    print(KMP_index(text, pattern))
    # print(get_next(tar))


if __name__ == '__main__':
    main()
