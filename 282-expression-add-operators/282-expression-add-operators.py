class Solution:
	def addOperators(self, num: str, target: int) -> List[str]:
		def backtrack(idx, prev,curr,value,s):
			if idx == n:
				if value == target and curr == 0:
					self.result.append(s)
				return

			curr = curr * 10 + int(num[idx])

			if curr > 0:
				backtrack(idx+1, prev,curr,value,s)

			if not s:
				backtrack(idx+1, curr, 0, value+curr, str(curr))
			else:
				backtrack(idx+1, curr, 0, value+curr, s+"+"+str(curr))
				backtrack(idx+1, -curr, 0, value-curr, s+"-"+str(curr))
				backtrack(idx+1, prev*curr, 0, value-prev+prev*curr, s+"*"+str(curr))

		n = len(num)
		self.result = []
		backtrack(0,0,0,0,"")

		return self.result