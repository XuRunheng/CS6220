import pandas as pd
def all_itemsets(file):
    df = pd.read_csv(file)
    uniqueList = df.reset_index().drop_duplicates().toList()
    ret = subsets(uniqueList)
    print(ret)
    return ret;

def subsets(self, nums):
    ans = []
    path = []
    n = len(nums)
    def dfs(i):
        if i == n:
            ans.append(path.copy())
            return
        dfs(i + 1)
        path.append(nums[i])
        dfs(i + 1)
        path.pop() 
    dfs(0)
    return ans

all_itemsets("example.csv")
