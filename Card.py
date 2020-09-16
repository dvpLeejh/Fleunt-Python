import collections #파이썬의 범용 내장컨테이너에 대한 대안을 제공하는 특수 컨테이너 데이터형을구현


Card =  collections.namedtuple('Card', ['rank', 'suit'])
#이름 붙은 필드를 갖는 튜플 서브클래스를 만들기위한 팩토리함

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    #2~10의 문자열 자료형, 'J','Q','K','A'가 저장됨
    suits = 'spades diamonds clubs hearts'.split()
    #spilt메소드에 아무값도 넣어주지 않으면 공백을 기준으로 문자열을 나눈다.-> suits는 리스트 자료형이됨
    def __init__(self):
        self._cards=[Card(rank, suit) for suit in self.suits 
                                    for rank in self.ranks]
    #중첩for문, ranks가 2부터A까지 한바퀴돌면 그뒤에 suits가 다음 suit를 불러들인다.
    def __len__(self):
        return len(self._cards)
    #전체 카드의 장수를 반환
    def __getitem__(self, position):
        return self._cards[position]
    #몇번째 카드가 무슨카드인지 반환

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
