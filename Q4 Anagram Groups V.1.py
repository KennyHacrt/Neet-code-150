class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new={}
        store=[]
        index=0
        if len(strs)==1 and strs[0]=="":
            return [[""]]
        for i in range(len(strs)):
            sort=''.join(sorted(strs[i]))
            if sort not in new:
                new[sort]=index
                index+=1
                store.append([])
            store[new[sort]].append(strs[i])
        return store
