

def insert_sort(nums):  # 稳定排序
    n = len(nums)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, n):
        # j=[1,2,3,,n-1]
        # i 代表内层循环起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置中
        '''
        while i > 0:# i=j,j-1,j-2...1
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                i -= 1
            else:
                break
        '''
        # range(j,0,-1)意思是从列表的下标为j的元素开始，倒序取到下标为0的元素（但是不包括下标为0元素）
        for i in range(j, 0, -1):
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
            else:  # 最优时间复杂度O(n)
                break
    return nums


def shell_sort(nums):
    n = len(nums)
    # 初始间隔
    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap-1, -gap):

                if nums[j] < nums[j-gap]:
                    nums[j], nums[j-gap] = nums[j-gap], nums[j]
                else:
                    break
        gap //= 2
    return nums


nums = [1, 4, 7, 8, 5, 2, 3, 6, 9, 0]
print('无序序列:', nums)
print('插入排序:', insert_sort(nums))
print('希尔排序:', shell_sort(nums))
