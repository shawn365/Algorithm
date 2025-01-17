class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor = 0
        for num in derived:
            xor ^= num
            
        if xor == 0:
            return True
        else:
            return False