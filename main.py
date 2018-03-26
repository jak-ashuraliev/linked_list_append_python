
# Linked list is a linear data structure and element are linked using pointers
# Advantages? Dynamic size, saves memory, can live anywhere in the memory, ease of insertiong and deletion

# Linked list consists of nodes
# Each node consists of a value and a pointer to the next node
# node => node => node => node = None

# Starting node of linked list is referred to as head
# Ending node of linked list is referred to as tail

# A complete working Python program to demonstrate all
# insertion methods of linked list

# Node class / function to initialize the node object
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # assign data
		self.next = None # initialize next as none/null

# Linked List class / function to initialize the head / starting point
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

    ### APPEND METHOD ###
	def append(self, new_data):

        # Create a new Node
        # Put in the data
        # Set next to None
		new_node = Node(new_data)

       	# Check if the linked list is empty, then make the new node as head
		if self.head is None:
			self.head = new_node
			return

		# Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# Change the next of last node
		last.next = new_node


	# Utility function to print the linked list
	def printList(self):
		temp = self.head
		while (temp):
			print temp.data,
			temp = temp.next


# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
	llist = LinkedList()

	# Insert / Append 5
	llist.append(5)

	# Insert / Append 4 So linked list becomes 5-> 4->None
	llist.append(4)


	#print the list
	llist.printList()

	
	
