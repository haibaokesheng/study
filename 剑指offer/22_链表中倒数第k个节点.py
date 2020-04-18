# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 11:11:16 2020

@author: haibao
"""

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

# 打印节点函数
def printlist(head):
    cur = head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next

def build():
    i = 1
    head = Node()
    temp = None
    cur = head
    while i<8:
        temp = Node()
        temp.data = i
        cur.next = temp
        cur = cur.next  ########实际是将cur引用的位置从当前节点移动到下一节点
        i += 1
    return head
    
# 找出第K个节点的值
def findk(head,k):
    if head ==None or head.next ==None:
        return None
    slow = Node()
    fast = Node()
    slow = head.next
    fast = head.next
    i = 0
    while i<k and fast!=None:
        fast = fast.next
        i += 1
    if i<k:
        return None
    while fast!=None:
        slow = slow.next
        fast = fast.next
    return slow

def getKthFromEnd(head,k):
    fast = slow = head
    while k>0:
        if fast == None: #链表节点数小于k的情况
            return None
        fast = fast.next
        k-=1
    while fast!=None:
        slow = slow.next
        fast = fast.next
    return slow
        

if __name__ =="__main__":
    head = build()
    result = None
    print("链表:")
    printlist(head)
#    result=findk(head,3)
    result=getKthFromEnd(head,3)

    if result!=None:
        print("\n链表倒数第3个元素为："+str(result.data))
