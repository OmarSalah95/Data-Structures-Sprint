import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Is this solution O(n2)?? This seems like an insane way to go about this, but Others seem similarly nuts.
# First thing to come to mind being I would like to cut this down to n log n at the least if not log n. If I want to do so
# I am going to need both of those long lists to be sorted, and issue in and of itself with its own complexity in the best of cases
# being Log n,
# I am going to need a more robust algorithmicly architected data structure to make this possible. I think a graph would work best
# But a Binary Searhc tree will work great for this for now
"""for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)"""
# for name in names_2:     # This is O(n) as we iterate and repeat this step
#     if name in names_1:
#         duplicates.append(name)

class BinarySearchTree:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def insert(self, name):
        if self.name < name:
            if self.right:
                self.right.insert(name)
            else:
                self.right = BinarySearchTree(name)
        elif self.name > name:
            if self.left:
                self.left.insert(name)
            else:
                self.left = BinarySearchTree(name)
        else: 
            duplicates.append(name)


bst = BinarySearchTree(names_1[0])
for name in names_1[1:]+names_2:
    bst.insert(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

