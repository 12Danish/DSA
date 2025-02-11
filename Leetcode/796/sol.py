class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        if s == goal:
            return True

        temp = s
        temp_char = ""
        for x in range(len(s)):
            temp_char = temp[0]
            temp = temp[1:]
            temp += temp_char

            if temp == goal:
                return True

        return False
