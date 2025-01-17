class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M":1000, "D": 500, "C": 100,"L":50, "X":10, "V": 5, "I":1}
        answer = 0

        for i in range(len(s) - 1):
            current_num = dic[s[i]]
            next_num = dic[s[i + 1]]
            if current_num >= next_num:
                answer += current_num
            else:
                answer -= current_num
        answer += dic[s[-1]]

        return answer