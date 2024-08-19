class Solution:
    def distMoney(self, money: int, children: int) -> int:
        money -= children

        if money < 0:
            return -1

        if money % 7 == 0 and money // 7 == children:
            return children

        if money % 7 == 3 and money // 7 == children - 1:
            return children - 2

        return min(money // 7, children - 1)