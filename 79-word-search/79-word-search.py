class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		rows, cols = len(board), len(board[0])
		path = set()

		def dfs(r, c, idx):
			if idx == len(word):
				return True
			if r >= rows or r < 0 or c >= cols or c < 0 or word[idx] != board[r][c] or (r, c) in path:
				return False
			path.add((r, c))
			res = (dfs(r + 1, c, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r, c - 1, idx + 1))
			path.remove((r, c))
			return res

		for r in range(rows):
			for c in range(cols):
				if dfs(r, c, 0): return True

		return False