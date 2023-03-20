class Atm(object):
    def __init__(self,atmcard,atmnumber):
        self.atmcard=atmcard
        self.atmnumber=atmnumber
    def CashWithdrawl(self):
        print("withdrawing cash")
    def BalanceEnquiry(self):
        print('enquiring balance')
dummy=Atm(232,323)
print(dummy.atmcard)