# Linked list is a linear data structure and element are linked using pointers
# Advantages? Dynamic size, saves memory, can live anywhere in the memory, ease of insertiong and deletion

# Linked list consists of nodes
# Each node consists of a value and a pointer to the next node
# node => node => node => node = None

# Starting node of linked list is referred to as head
# Ending node of linked list is referred to as tail

# Node class / function to initialize the node object
class Node:
	def __init__ (self, data):
  	self.data = data # assing data
    	self.next = None # initialize next as none/null
    
# LinkedList class / function to initialize the head = starting point
class LinkedList(sefl):
	# function to initialize the head
 	def __init__ (self):
 		self.head = None
  
 	### Append Method ###
  	def append(self, new_data):
  	
   	# Create a new node
   	# Put in the data
   	# Set next to None
    	new_node = Node(new_data)
    
   	# Check if the linked list is empty, then make the new node as head
   	if self.head is None:
    		self.head = new_node
     		return
      
    	# Else tarverse till the last node
    	last = self.head
    	while (last.next):
    		last = last.next
    
    	# Change the next of last node
    	last.next = new_node
   
	# Unitilty function to print the linked list
  	def printList():
  		temp = self.head
    		while (temp):
    		print temp.data, # print data
      		temp = temp.next # point to next

# Code execution statrs here
if __name__ = '__main__':

	# start with the empty list
  	llist = LinkedList()
  
	# insert / append 5
	llist.append(5)

	# insert / append 6
	llist.append(6)

	#print the list
	llist.printLisst()
