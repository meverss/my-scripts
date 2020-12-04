"""
Title:    Poker Hand
Author:   MeVeRs

Description:
Output the rank of the give poker hand.

Input Format:
A string, representing five cards, each indicating the value
Possible card values are: 2 3 4 5 6 7 8 9 10 J Q K A
Suites:  H (Hearts), D (Diamonds), C (Clubs), S (Spades)
For example, JD indicates Jack of Diamonds.

Sample Input:
9S 10H JC AC KH
"""

cards = input().upper() or '6S 10d Jh AS kS'.upper()
cards = cards.split(' ')

def check_hand(hand):
  values = ['2','3','4','5','6','7','8',
           '9','10','J','Q','K','A']
  suites = ['H','D','C','S']
  ssuites = ['♥️' , '♦️','♣️' , '♠️']
  chhand = ' '.join(hand.copy())
  k = list(chhand.count(hand[x][:-1]) for x in range(5))
  s = list(chhand.count(hand[x][-1]) for x in range(5))
  st = list(values.index(hand[x][:-1]) for x in range(5))
  st.sort()
  straight = st[0] == st[1]-1 == st[2]-2 == st[3]-3 == st[4]-4
  myhand = []
  for mh in range(5):
    myhand.append(f"{hand[mh][:-1]}{ssuites[suites.index(hand[mh][-1])]}")
  myhand.sort(key=(lambda x: values.index(x[:-2])))
  myhand = ' '.join(myhand)
  print(myhand)

  if k.count(1) == 5 and s.count(5) == 0 and not straight:
    return ('High Card')
  elif k.count(2) == 2 and k.count(1) == 3:
     return ('One Pair')
  elif k.count(2) == 4:
     return ('Two Pairs')
  elif k.count(3) == 3 and k.count(1) == 2:
     return ('Three of a Kind')
  elif straight and s.count(5) == 0:
     return ('Straight')
  elif s.count(5) == 5 and not straight:
     return ('Flush')
  elif k.count(2) == 2 and k.count(3) == 3:
     return ('Full House')
  elif k.count(4) == 4:
     return ('Four of a Kind')
  elif s.count(5) == 5 and straight and not all(x in st for x in range(8,13)):
     return ('Straight Flush')
  elif all(x in st for x in range(8,13)) and s.count(5) == 5:
     return ('Royal Flush!!!')

print(check_hand(cards))
