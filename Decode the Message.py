class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict1 = {}
        start = 97
        decoded = ""

        for i in key:
            if i == " ":
                continue
            elif i not in dict1:
                dict1[i] = chr(start)
                start += 1
            else:
                continue

        for i in message:
            if i == " ":
                decoded += i
            else:
                decoded += dict1[i]

        return decoded