#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.44%)
# Likes:    670
# Dislikes: 0
# Total Accepted:    109.7K
# Total Submissions: 293K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
# 
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，
        则左半段是有序的，我们只要在有序的半段里用首尾两个数组来判断目标值是否在这一区域内，
        这样就可以确定保留哪半边了
        '''
        if not nums:
            return -1
        left = 0
        right = len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            print(mid)
            if nums[mid]<nums[right]:#[mid,right] 有序
                #if nums[mid]<target:
                if nums[mid]<target<=nums[right]: #[mid,right]
                    left = mid+1
                else:
                    right = mid  #[left,mid]
            else:  #[left,mid]  有序    
                if nums[left]<=target<=nums[mid]:#说明target位于mid的左侧
                    right = mid            
                else:
                    left = mid +1
        return -1 if nums[left]!=target else left
# @lc code=end

