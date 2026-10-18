class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pass
        m = len(nums)
        answer = []
        i,j = 0,n
        while i<n and j<m :
            answer.append(nums[i])
            answer.append(nums[j])
            i+=1
            j+=1
        return answer