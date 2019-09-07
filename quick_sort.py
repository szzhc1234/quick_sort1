# -*- coding:utf-8 -*-

# 快速排序
def sort(list01,low,height):
    x=list01[low]
    while low<height:
        if list01[height]>=x and height>low:
            height-=1
        list01[low]=list01[height]
        if list01[low]<x and low<height:
            low+=1
        list01[height]=list01[low]
    list01[low]=x
    return low

def quik(list01,low,hegiht):
    if low<hegiht:
        key=sort(list01,low,hegiht)
        quik(list01,key+1,hegiht)
        quik(list01,low,hegiht-1)
    return list01

list02=[3,6,5,4,8,9,10]
quik(list02,0,len(list02)-1)
print(list02)


# 快排
def qucik_sort(alist):
    if len(alist) <= 1:
        return alist
    return qucik_sort([i for i in alist[1:] if i < alist[0]]) + alist[0:1] + qucik_sort([i for i in alist[1:] if i >= alist[0]])


ls = [22, 21, 34, 65, 12, 89, 3, 9, 66]
print(qucik_sort(ls))

