# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 09:53:40 2020

@author: haibao
2020.3.4
"""
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
def build():
    i = 1
    head = Node()
    temp = None
    cur = head
    while i<8:
        temp = Node()
        temp.data = i
        cur.next = temp
        cur = cur.next
        i += 1
    return head

def printlist(head):
    cur = head.next
    while cur!=None:
        print(cur.data)
        cur=cur.next

def ReverseList(head):
# 申请两个节点，pre和 cur，pre指向None
    pre = None
    cur = head #当前节点
    if cur == None or cur.next == None:
        return head
    while cur:
        # 记录当前节点的下一个节点
        tmp = cur.next 
        # 然后将当前节点指向pre
        cur.next = pre 
        # pre和cur节点都前进一位
        pre = cur
        cur = tmp    
    return pre
if __name__ =="__main__":
   head = build()
   print("链表:")
   printlist(head)
   print("反转链表:")
   printlist(ReverseList(head))

       
        
    
