
class ListNode:
    def  __init__(self,x):
        self.val = x
        self.next = None
        
def printChain(node):
    while node:
        print(node.val,end=' → ')
        node = node.next
        
def printListFromTailToHead(listNode):
    ret = []
    Ptmp = listNode
    while Ptmp:
        ret.insert(0,Ptmp.val)
        Ptmp = Ptmp.next
    return ret

if __name__=="__main__":
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
  
    printChain(l1)
   # print(printListFromTailToHead(l1))
