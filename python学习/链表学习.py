
class Node():
    def __init__(self,elem):
        self.elem = elem
        self.next = None

class SingleLinkList():
    def __init__(self,node =None):
        self.__head = node

    def is_empty(self):
        return self.__head == None
    
    def length(self):
        cur = self.__head # cur 和 head指向同一地址
        count = 0
        while cur:
            count+=1
            cur = cur.next #从右往左看
        return count
    
    def travel(self):
        cur = self.__head
        while cur:
            print(cur.elem,end=' ')
            cur = cur.next
        print('')

    def add(self,item):
        node = Node(item)
        node.next = self.__head
        self.__head = node 

    def append(self,item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        node = Node(item)
        if pos<=0:
            self.add(item)
        elif pos>(self.length()-1):#不包含=号
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count<(pos-1):
                pre = pre.next
                count+=1
            #当循环退出后，pre指向pos-1位置      
            node.next = pre.next
            pre.next = node
    
    def search(self,item):
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False 
    
    def remove(self,item):
        cur = self.__head
        pre = None
        while cur:
            if cur.elem == item:
                #先判断是否头节点
                if cur == self.__head:
                    self.__head = cur.next
                else:    
                    pre.next = cur.next
                break
            else:    
                pre = cur #顺序不能反
                cur = cur.next

if __name__ == "__main__":
    l1 = SingleLinkList()
    print(l1.is_empty())
    print(l1.length())
    l1.append(1)
    print(l1.is_empty())
    print(l1.length())
    l1.append(2)
    l1.append(3)
    l1.add(10)
    l1.append(4)
    l1.insert(-1,55)
    l1.insert(262,87)
    l1.insert(3,58)
    l1.travel()
    l1.remove(55)
    l1.travel()

        

