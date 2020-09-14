import collections #파이썬의 범용 내장컨테이너에 대한 대안을 제공하는 특수 컨테이너 데이터형을구현


Card =  collections.namedtuple('Card', ['rank', 'suit'])
#이름 붙은 필드를 갖는 튜플 서브클래스를 만들기위한 팩토리함

class FrenchDech:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self.cards=[Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, posistion):
        return self.cards[position]
     
