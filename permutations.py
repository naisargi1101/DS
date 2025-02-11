import copy
class Solution:
    def permute(self, nums):
        perms = [[]]
        for i in nums:
            new_perm = []
            for p in perms:
                for j in range(len(p)+1):
                    p_copy = copy.deepcopy(p)
                    p_copy.insert(j,i)
                    new_perm.append(p_copy)
            perms=new_perm
        return perms
        