class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save= defaultdict(list)
        for i in range(len(strs)):
            count=[0]*26
            for j in strs[i]:
                count[ord(j)-97]+=1
            save[tuple(count)].append(strs[i])
        strs=[]
        for i in save:
            strs.append(save[i])
        return strs

#or shorter pythonic ver

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        save= defaultdict(list)
        for i in range(len(strs)):
            count=[0]*26
            for j in strs[i]:
                count[ord(j)-97]+=1
            save[tuple(count)].append(strs[i])
        return save.values()

        
