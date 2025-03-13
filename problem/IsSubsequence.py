class IsSubsequence:

    def isSubsequence(selfself, s: str, t: str) -> bool:

        lenS = len(s)
        lenT = len(t)

        if lenS > lenT:
            return False

        if lenS == 0:
            return True

        sequenceCounter = 0

        for i in range(lenT):
            if s[sequenceCounter] == t[i]:
                sequenceCounter += 1
            if sequenceCounter == lenS:
                return True

        return False


if __name__ == '__main__':
    sol = IsSubsequence()
    print(sol.isSubsequence("abc", "ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))
