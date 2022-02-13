class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
      groups = [None for _ in accounts]
      
      for i in range(len(accounts)):
        groups[i] = set(accounts[i][1:])
        
      
      while True:
        isMerged = False        
        for i in range(len(groups)):
          if not groups[i]:
            continue
            
          for j in range(i+1, len(groups)):
            if not groups[j]:
              continue
            
            if groups[i] & groups[j]:
              groups[i] = groups[i] | groups[j]
              groups[j] = None
              isMerged = True
              break

        if not isMerged:
          break
          
      ans = []
      for i in range(len(groups)):
        if not groups[i]:
          continue
        name = accounts[i][0]
        values = sorted(list(groups[i]))
        ans.append([name]+values)

      return ans