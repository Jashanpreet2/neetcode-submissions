class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        hand.sort(reverse=True)
        beg, next = hand.pop(), None

        while len(hand) > 0:
            for i in range(groupSize):
                if count[beg+i] == 0:
                    return False
                count[beg+i] -= 1
                next = beg+i if next is None and count[beg+i] > 0 else next

            beg, next = next, None
            if beg is None:
                while len(hand) > 0 and count[hand[-1]] == 0:
                    hand.pop()
                if len(hand) == 0:
                    return True
                beg = hand.pop()
        return True
