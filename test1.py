'''class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def maxPathSum(root: TreeNode) -> int:
	res = [root.val]
	
	def dfs(root):
		if not root:
			return 0
		
		leftMax = dfs(root.left)
		rightMax = dfs(root.right)
		# in case of negative
		leftMax = max(leftMax, 0) 
		rightMax = max(rightMax, 0)
		
		# compute max path sum WITH split
		res[0] = max(res[0], root.val + leftMax + rightMax)
		
		return root.val + max(leftMax, rightMax)
	dfs(root)
	return res[0]
 

# Driver code
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
print(maxPathSum(root))'''

from typing import List
import collections
from collections import deque
import heapq
'''
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
	if endWord not in wordList:
		return 0
	
	nei = collections.defaultdict(list) # adj list
	wordList.append(beginWord)
	for word in wordList:
		for j in range(len(word)):
			pattern = word[:j] + "*" + word[j + 1:] # e.g. hot => *ot, h*t, ho*
			nei[pattern].append(word)
		
		# bfs
		visit = set([beginWord]) # start at beginWord
		q = deque([beginWord])
		res = 1
		while q:
			for i in range(len(q)):
				word = q.popleft()
				if word == endWord:
					return res
				for j in range(len(word)):
					pattern = word[:j] + "*" + word[j + 1:] # hit => *it, h*t
					for neiWord in nei[pattern]: # neiWord = hot match above * pattern
						if neiWord not in visit:
							visit.add(neiWord)
							q.append(neiWord)
			
			res += 1
		return 0
'''
def isMatch(s: str, p: str) -> bool:
	# TOP-Down Memoization
	
	cache = {}
	
	def dfs(i, j):
		if (i, j) in cache:
			return cache[(i, j)]
		if i >= len(s) and j >= len(p): # found solution
			return True
		if j >= len(p):
			return False
			
		match = i < len(s) and (s[i] == p[j] or p[j] == ".")
		if (j + 1) < len(p) and p[j + 1] == "*":
			cache[(i, j)] = (dfs(i, j + 2) or # dont use *
						    (match and dfs(i + 1, j))) # use *
			return cache[(i, j)]
		if match:
			cache[(i, j)] = dfs(i + 1, j + 1)
			return cache[(i, j)]
		
		cache[(i, j)] = False
		return False
	
	return dfs(0, 0)
		
print(isMatch("aaabaaa", "a*b*a*"))