class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        hand.sort(reverse=True)
        print(hand)
        beg = hand.pop()

        while len(hand) > 0:
            next = None
            if beg is None:
                while len(hand) > 0 and count[hand[-1]] == 0:
                    hand.pop()
                if len(hand) == 0:
                    return True
                beg = hand.pop()
            for i in range(groupSize):
                if count[beg+i] == 0:
                    return False
                count[beg+i] -= 1
                if next is None and count[beg+i] != 0:
                    next = beg+i

            beg = next
        return True
