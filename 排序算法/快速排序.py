
nums = [1, 4, 7, 8, 5, 2, 3, 6, 9, 0]


def QuickSort(nums, start, end):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:  #  只有一个元素的时候
        i, j = start, end
        # 设置基准数
        base = nums[i]

        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            # 当 i 和 j 相等时候，while不执行，交换2次，不影响
            while (i < j) and (nums[j] >= base):
                j = j - 1
            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            nums[i] = nums[j]
            # 同样的方式比较前半区
            while (i < j) and (nums[i] <= base):
                i = i + 1
            nums[j] = nums[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        nums[i] = base
        # 递归前后半区 不能使用切片的方式
        QuickSort(nums, start, i - 1)
        QuickSort(nums, j + 1, end)
    return nums


print(QuickSort(nums, 0, len(nums)-1))
