import re
def solution(myStr):
    answer = [s for s in re.split("[abc]", myStr) if s]
    
    return answer if answer else ["EMPTY"]