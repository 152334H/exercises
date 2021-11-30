from typing import List
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # create a ufds of emails and their names
        ufds = {i:i for i in range(len(accounts))}
        def find(x):
            if ufds[x] != x: ufds[x] = find(ufds[x])
            return ufds[x]
        def union(x, y): ufds[find(x)] = find(y)
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email not in ufds: ufds[email] = i
                else: # union the two emails
                    union(email, i)
        ans = collections.defaultdict(list)
        for i,ls in enumerate(accounts):
            ans[find(i)] += ls[1:]
        return [[accounts[i][0]] + list(sorted(set(emails))) for i, emails in ans.items()]



s = Solution()
for (inp,out) in [
    ([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]], [[]])
    ]:
        print(s.accountsMerge(inp))
