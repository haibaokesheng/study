# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 14:05:11 2020

@author: haibao
"""
class ListNode:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
# 单链表类
class SingleLinkedList():
    # 初始化
    def __init__ (self):
        self.head = None

    # 判断链表是否为空
    def is_empty(self):
        if self.head is None:
            return True
  
    # 增加一个新的结点
    def append(self,new_value):
        node = ListNode(new_value)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    # 遍历整个链表，并将其值存在一个列表中
    def travel(self):
        cur = self.head
        ls = []
        while cur is not None:
            ls.append(cur.data)
            cur =cur.next
        return ls
        
    # 自行设置头节点，遍历链表，并将其值存在一个列表中    
    def travelSetHead(self,pHead):
        cur = pHead
        ls = []
        while cur is not None:
            ls.append(cur.data)
            cur =cur.next
        return ls


def mergeTwoLists(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    pre = None
    if l1.data<l2.data:
        pre = l1
        pre.next = mergeTwoLists(l1.next,l2)
    else:
        pre = l2
        pre.next = mergeTwoLists(l1,l2.next)
    return pre
    
if __name__=="__main__":
    SLL1 = SingleLinkedList()
    for i in range(10,1,-2):
        SLL1.append(i)
    print(SLL1.travel())
    SLL2 = SingleLinkedList()
    for i in range(5,0,-2):
    	SLL2.append(i)
    print(SLL2.travel())
    
    pMergeHead = mergeTwoLists(SLL1.head,SLL2.head) 
    print(SLL1.travelSetHead(pMergeHead))
