class ipad:

    def __init__(self):
        self.__price=1000

    def sell(self):
        print("selling priceis:",self.__price)

    def mprice(self,newprice):
        self.__price=newprice

i=ipad()
i.sell()

i.__price=10000
i.sell()
i.mprice(150000)
i.sell()