class Node:
    def __init__(self,data):
        self.data = data
        self.next =None
class Linkedlist:
    def __init__(self):
        self.head = None
    def insertnode(self,Node):
        if self.head == None:
            self.head = Node
        else:
            lastnode = self.head
            while lastnode !=None:
                lastnode = lastnode.next
            lastnode.next = Node
    def Printlist(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
    def inser_at_beggining(self,Node):
        temp = self.head
        self.head = Node
        Node.next = temp
        self.head = Node
    def insert_at_last(self,Node):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node
    def count_nodes(self):
        count1 = 0
        temp = self.head
        while(temp != None):
            count1 += 1
            temp = temp.next
        print(count1)
    def inser_be(self,node_number,Node):
        count1 = 0
        temp = self.head
        while(temp != None):
            count1 += 1
            temp = temp.next
        if self.head == None:
            return 'node is empty'
        elif count1 < node_number:
            return 'linked list is shorter then your fiven number'
        else:
            temp = self.head
            count_nodes = 1
            while count_nodes< node_number:
                if count_nodes == 1:
                    temp = temp.next
                    temp1 = self.head
                else:
                    temp = temp.next
                    temp1 = temp1.next    
                count_nodes += 1
            temp1.next = Node
            temp1 = temp1.next
            temp1.next = temp
print('***************************select your coice *****************************')
print('1:- enter node')
print('2:- insert at beggining')
print('3:- insert at last')
print('4:- insert b/w')
print('5:- count nodes')

firstnode = Node('adarsh')
linklist = Linkedlist()
linklist.insertnode(firstnode)
# linklist.Printlist()
seconnode = Node('singh')
linklist.inser_at_beggining(seconnode)
# linklist.Printlist()
thirdnode = Node('chauhan')
linklist.insert_at_last(thirdnode)
# linklist.Printlist()
linklist.count_nodes()
fourtnode = Node('rajat')
linklist.inser_be(2,fourtnode)
linklist.Printlist()
linklist.count_nodes()
