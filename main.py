# A complete working Python program to demonstrate all
# insertion methods of linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null

# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function is defined in Linked List class
	# Appends a new node at the end. This method is
	# defined inside LinkedList class shown above */
	def append(self, new_data):

		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
		new_node = Node(new_data)

		# 4. If the Linked List is empty, then make the
		# new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# 6. Change the next of last node
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

	# Insert 5. So linked list becomes 5->None
	llist.append(5)

	# Insert 6 at the end. So linked list becomes 5->6->None
	llist.append(6)

	print 'Created linked list is:',
	llist.printList()
