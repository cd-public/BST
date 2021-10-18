# Autograder

# This will attempt to perform intended tasks for Stack. It will only use naturals, for simplicity.
# It is not required that your stack work with values other than naturals or only with naturals.
# For each task, the autograder will:
#  - Define some expected behavior for some use case
#  - Perform the use case
#  - Award "points" if the result is as expected
#  - Either not award points (not too bad) or cause an error (pretty bad) if the result is not as expected
#    NOTE: Exception handling here could manage these errors, but it can be helpful to see them as well!


# This is a script to do the tests and print out what's happening
def singleTest(desc, target, val, pts):
	print("AUTOGRADER: " + desc)
	print(" - Expected Value: " + str(target))
	print(" - Observed Value: " + str(val))
	score = 0
	if (val == target):
		score = 5
		pts = pts + 5
	print("POINTS: This section: " + str(score).zfill(2) + "/05 Total: " + str(pts).zfill(3) + "/100\n")	
	return pts

# my favorite example of a BST
def exBST():
	return BST(5).insert(3).insert(7).insert(2).insert(4).insert(6).insert(8)
	
points = 0

print("\n --- AUTOGRADER: STACK ---\n")
# from bst import node as BST # can test internal nodes using this line
from bst import BST
b = BST(5)

print("\nAUTOGRADER: Singleton BST Testing: 30 pts\n")
points = singleTest("Checking BST(5).size()  is one", 1, b.size(), points)
points = singleTest("Checking BST(5).depth() is one", 1, b.depth(), points)
points = singleTest("Checking BST(5).contains(5) is True", True, b.contains(5), points)
points = singleTest("Checking BST(5).getMin() is 5", 5, b.getMin(), points)
points = singleTest("Checking BST(5).getMax() is 5", 5, b.getMax(), points)
b = b.insert(3)
points = singleTest("Checking BST(5) is still a stack after inserting 3.", type(BST(5)), type(b), points)

print("\nAUTOGRADER: Doubleton Stack Testing: 30 pts\n")
points = singleTest("Checking that after insert 3 that 5 is contained", True, b.contains(5), points)
points = singleTest("Checking that after insert 3 that 3 is contained", True, b.contains(3), points)
points = singleTest("Checking .size()  is two", 2, b.size(), points)
points = singleTest("Checking .depth() is two", 2, b.depth(), points)
points = singleTest("Checking BST(5).getMin() is 3", 3, b.getMin(), points)
points = singleTest("Checking BST(5).getMax() is 5", 5, b.getMax(), points)

print("\nAUTOGRADER: BST Remove Testing: 40 pts\n")
b = exBST()
points = singleTest("Checking example is of size 7", 7, b.size(), points)
points = singleTest("Checking example is of depth 3", 3, b.depth(), points)
points = singleTest("Checking root removal: example.remove(5) should not contain 5", False, b.remove(5).contains(5), points)
points = singleTest("Checking root removal: example.remove(5) contains other values", True, all([b.contains(n) for n in [2,3,4,6,7,8]]), points)
b = exBST().remove(2)
points = singleTest("Checking leaf removal: example.remove(2) should not contain 2", False, b.contains(2), points)
points = singleTest("Checking root removal: example.remove(2) contains other values", True, all([b.contains(n) for n in [3,4,5,6,7,8]]), points)
b = exBST().remove(3)
points = singleTest("Checking internal removal: example.remove(3) should not contain 3", False, b.contains(3), points)
points = singleTest("Checking internal removal: example.remove(3) contains other values", True, all([b.contains(n) for n in [2,4,5,6,7,8]]), points)



	