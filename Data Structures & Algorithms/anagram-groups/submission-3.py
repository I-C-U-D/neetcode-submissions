class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        single = []
        group = []
        
        if len(strs) < 2:
            group.append(strs)
            return group

        strs = sorted(strs)
     
        for i in range(len(strs)):
            group_temp = []
            if strs[i] not in single:
                group_temp.append(strs[i])
                single.append(strs[i])
            for j in range(i+1,len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    if strs[j] not in single or strs.count(strs[j]) != single.count(strs[j]):
                        group_temp.append(strs[j])
                        single.append(strs[j])
            if group_temp:
                group.append(group_temp)
        return group

