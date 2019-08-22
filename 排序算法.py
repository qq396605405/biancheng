#冒泡排序
#1. 算法步骤
'''1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。

2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

3.针对所有的元素重复以上的步骤，除了最后一个。

4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较'''
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#选择排序
'''1.首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

2.再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

3.重复第二步，直到所有元素均排序完毕。'''

def selectionSort(arr):
    for i in range(len(arr)):
        weizhi=arr[i:].index(min(arr[i:]))
        a=arr[i+weizhi]
        b=arr[i]
        arr[i],arr[i+weizhi]=a,b
    return arr
print(selectionSort([3,2,1,5,4,7,6,10,9,1,2,3]))


#插入排序

1. 算法步骤

'''将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。

从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）
'''

def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr
[3,5,1]







