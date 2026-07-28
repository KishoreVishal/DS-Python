class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
n1=Node(10)
n2=Node(20)
n3=Node(30)
n1.next=n2
n2.next=n3
head=n1
def display(head):
    temp=head
    while temp is not None:
        print(temp.data, end="->")
        temp=temp.next
    print("None")
print("Original Linked List")
display(head)
print("/nInsertion at Beginning")
new_node=Node(5)
new_node.next=head
head=new_node
display(head)
print("/nInsertion at Middle")
new_node=Node(15)
temp=head
while temp.data!=20:
    temp=temp.next
new_node.next=temp.next
temp.next=new_node
display(head)
print("/nInsertion at End")
n4=Node(40)
temp=head
while temp.next:
    temp=temp.next
temp.next=n4
display(head)
print("/nDeletion at Beginning")
head=head.next
display(head)
print("/nDeletion at Middle")
temp=head
while temp.next.data!=20:
    temp=temp.next
temp.next=temp.next.next
display(head)
print("/nDeletion at End")
temp=head
while temp.next.next:
    temp=temp.next
temp.next=None
display(head)
