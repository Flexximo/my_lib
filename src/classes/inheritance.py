class Gun():
    """@standard template for a weapon"""
    def __init__(self, bullet_n, weight, price, efficiencyRate):
        """INITIALIZE"""
        self.bullet_n = bullet_n
        self.weight = weight
        self.price = price
        self.efficiencyRate = efficiencyRate

    def shot(self):
        assert self.bullet_n >= 0, "number of bullets 0 or > 0"
        while(self.bullet_n >= 0):

            print("shooting", f"{self.bullet_n}", "left")
            if (self.bullet_n == 0):
                self.weight = self.weight - 10
                print(self.weight)
            self.bullet_n = self.bullet_n - 1





class Pistol(Gun):
    def __init__(self, bullet_n, weight, price, efficiencyRate, clip_size):
        super().__init__(bullet_n, weight, price, efficiencyRate)
        self.clip_size = clip_size

    def flash(self):
        print("flash used to flash", f"{self}")

if __name__ == "__main__":
    pistol = Pistol(10, 20, 300, 12, 17)
    pistol.shot()
    print(pistol.__sizeof__())
    print(pistol.__doc__)
