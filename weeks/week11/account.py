from __future__ import annotations

class Account:
    def __init__(self, gold):
        '''
        Creates an account with gold based on amount provided
        '''
        self.gold = gold

    def addGold(self, added_gold: int) -> None:
        self.gold += added_gold

    def zeroGold(self) -> None:
        self.Gold = 0

    def doubleGold(self) -> None:
        self.gold *= 2

    def __eq__(self, other: Account) -> bool:
        '''
        Return bool if accounts have the same amount of gold
        '''
        return isinstance(other, Account) and self.gold == other.gold
    
    def __lt__(self, other: Account) -> bool:
        '''
        Return bool if self less gold than other
        '''
        return isinstance(other, Account) and self.gold < other.gold
    
a1 = Account(500)
a2 = Account(500)