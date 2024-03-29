class Solution:
    def isValid(self, s: str) -> bool:
        new_arr = []
        if len(s) % 2 != 0:
            return False
        elif s[0] == "}" or s[0] == "]" or s[0] == ")":
            return False
        else:
            for i in range(len(s)):
                print(i)
                if s[i] == "{":
                    new_arr.append(s[i])
                elif s[i] == "[":
                    new_arr.append(s[i])
                elif s[i] == "(":
                    new_arr.append(s[i])
                elif s[i] == "}":
                    try:
                        if new_arr[-1] == "{":
                            new_arr.pop()
                        else:
                            return False
                    except IndexError:
                        return False
                elif s[i] == "]":
                    try:
                        if new_arr[-1] == "[":
                            new_arr.pop()
                        else:
                            return False
                    except IndexError:
                        return False
                elif s[i] == ")":
                    try:
                        if new_arr[-1] == "(":
                            new_arr.pop()
                        else:
                            return False
                    except IndexError:
                        return False
            if len(new_arr) == 0:
                return True
            else:
                return False



