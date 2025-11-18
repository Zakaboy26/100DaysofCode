#Flowchart
'''START
 │
 ▼
Display game logo
 │
 ▼
Deal two cards to player
Deal two cards to dealer
 │
 ▼
Show player's cards and one of dealer's cards
 │
 ▼
Check for BLACKJACK (21):
 ├── If player has 21 → Player wins (unless dealer also has 21 → draw)
 └── Else → continue
 │
 ▼
PLAYER'S TURN:
 ├── Ask: "Type 'y' to get another card, 'n' to pass."
 │      ├── If 'y': draw new card → update total
 │      │       ├── If total > 21 and has Ace (11): convert Ace to 1
 │      │       ├── If still > 21 → Player busts → Dealer wins
 │      │       └── Otherwise → repeat
 │      └── If 'n': pass turn to dealer
 │
 ▼
DEALER'S TURN:
 ├── While dealer total < 17:
 │        ├── Draw card
 │        ├── Adjust for Ace if needed
 │        └── Update total
 │
 ▼
COMPARE SCORES:
 ├── If dealer > 21 → Player wins
 ├── If player > dealer → Player wins
 ├── If player == dealer → Draw
 └── Else → Dealer wins
 │
 ▼
Ask: "Do you want to play again?"
 ├── If yes → clear screen, restart game
 └── If no → END GAME
'''