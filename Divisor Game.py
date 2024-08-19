class Solution:
    def divisorGame(self, n: int) -> bool:
        player = "a"
        if n == 1:
            return False

        while n > 1:
            a = 1
            b = 1
            player = "a"
            if n % a == 0:
                n = n - a
                print("a", n)
            else:
                return False

            if n > 1:
                player = "b"
                if n % b == 0:
                    n = n - b
                    print("b", n)
                else:
                    return True
            else:
                return True

        if player == "a":
            return True
        else:
            return False



