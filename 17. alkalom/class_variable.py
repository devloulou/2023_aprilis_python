class HUF:
    euro_arfolyam = 380
    def __init__(self):
        self.money = 20_000
    
    def sell_deviza(self):
        return self.money / self.euro_arfolyam

if __name__ == '__main__':
    knh = HUF()
    otp = HUF()
    erste = HUF()


    # print(knh.sell_deviza())
    # print(otp.sell_deviza())
    # print(erste.sell_deviza())

    #  délután 2

    HUF.euro_arfolyam = 400

    print(knh.euro_arfolyam)
    print(otp.euro_arfolyam)
    print(erste.euro_arfolyam)
    print(HUF.euro_arfolyam)

    HUF.euro_arfolyam = 398
    knh.euro_arfolyam = 397.8 # itt megszünteted a referenciát a HUF.euro_arfolyam és a knh objektum között

    print(knh.euro_arfolyam)
    print(otp.euro_arfolyam)
    print(erste.euro_arfolyam)
    print(HUF.euro_arfolyam)

    print("######################")

    HUF.euro_arfolyam = 410

    knh.euro_arfolyam = HUF.euro_arfolyam

    HUF.euro_arfolyam = 420
    print(knh.euro_arfolyam)
    print(otp.euro_arfolyam)
    print(erste.euro_arfolyam)