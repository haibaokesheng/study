#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.14%)
# Likes:    607
# Dislikes: 0
# Total Accepted:    105.7K
# Total Submissions: 208.4K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        '''
        时间复杂度:O(nlogk)
        空间复杂度:O(k)
        '''
        if not lists:
            return
        import heapq
        quene = []
        dummy = ListNode(None)
       
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heapq.heappush(quene,head.val)
                head = head.next
        cur = dummy
        while quene:
            temp_node = ListNode(heappop(quene))
            cur.next = temp_node
            cur = temp_node  #当前指针移向下一个node
        return dummy.next
# @lc code=end

