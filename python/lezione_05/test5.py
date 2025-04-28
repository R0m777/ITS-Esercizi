def blackjack_hand_total(cards: list[int]) -> int:
    total = sum(cards)
    aces = cards.count(11)
    
    while total > 21 and aces > 0:
        total -= 10  
        aces -= 10
    
    return total

print(blackjack_hand_total([2, 3, 5]))
print(blackjack_hand_total([11, 5, 5]))
print(blackjack_hand_total([11,11]))