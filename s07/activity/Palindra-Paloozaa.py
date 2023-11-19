# Palindra-palooza
# Palindrome Checker
'''Implement modifications to the existing palindrome checker to handle palindromes
in sentences, considering spaces, punctuation, and capitalization.
'''
#Initiating the Class Node for Linked List
class Node:
    def __init__(self, check):
        self.data = check
        self.next = None
#Initiating the Class Stack
class Stack:
    def __init__(self):
        self.top = None
#Code for Pushing the Data
    def push(self, check):
        new = Node(check)
        if self.top is None:
            self.top = new
            self.top.next = None
        else:
            new.next = self.top
            self.top = new
#Code for Popping the data
    def pop(self):
        if self.top is None:
            print("Stack is empty")
        elif self.top.next is None:
            print("Popped element: ", self.top.data)
            print("--------------------------------")
            self.top = None
        else:
            temp = self.top
            print("Popped element: ", self.top.data)
            print("--------------------------------")
            self.top = temp.next
            temp = None
#Code for the palindrome Checker
    def Palindrome(self):
        cleaned = ""
        reversed  = ""
        #Code for detemining if the Stack is empty
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top

            while temp:
                cleaned = temp.data + cleaned
                temp = temp.next
            #Printing the sentence in Cleaned
            print(f"Your Sentence is Cleaned: {cleaned}")
            temp = self.top
            while temp:
                reversed += temp.data
                temp = temp.next
            #Printing the Sentence in Reverse
            print(f"Your Sentence is Reversed: {reversed}")
        #Initialization if the sentence is palindrome or not
        if cleaned == reversed:
            print(f"Your sentence: {User} is a palindrome")
        else:
            print(f"Your sentence: {User} is not palindrome")
    #Special Characters
    def sentence(self, aplha):
        punc = '''{}[];:'"\,<>./?%$#@!'''
        aplha = aplha.lower()
        aplha = aplha.strip()
        aplha = aplha.replace(" ","")
     # For Loop: For each character in the variable
        for element in aplha:
            if element in punc:
                aplha = aplha.replace(element, "")
        return aplha
x = Stack()
User = input("Enter your Sentence: ")
final = x.sentence(User)
for i in final:
    x.push(i)
x.Palindrome()
