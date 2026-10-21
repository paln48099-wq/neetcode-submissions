class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n,m = len(word1),len(word2)
        i,j =0,0
        result = []
        while i<n and j<m:
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        while i<n:
            result.append(word1[i])
            i+=1
        while j<m:
            result.append(word2[j])
            j+=1
        return "".join(result)