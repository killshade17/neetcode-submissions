class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list = []
        for i in s:
            list.append(i)
        for j in t:
            if j in list:
                list.remove(j)
        if not list:
            return True
        else:
            return False
