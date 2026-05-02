class Car:
    def __init__(self, make, model, sticker_price):
        self.make_name = make
        self.model_name = model
        self.sticker_price_amount = sticker_price

    def make(self):
        return self.make_name

    def model(self):
        return self.model_name

    def sticker_price(self):
        return self.sticker_price_amount

    def discount_price(self):
        return self.sticker_price_amount * 0.90


class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = 'N'
        self.sport_engine = 'N'
        self.sport_interior = 'N'

    def SportWheels(self):
        self.sport_wheels = 'Y'

    def SportEngine(self):
        self.sport_engine = 'Y'

    def SportInterior(self):
        self.sport_interior = 'Y'

    def pricewithoptions(self):
        price = self.discount_price()

        if self.sport_wheels == 'Y':
            price += 1000

        if self.sport_engine == 'Y':
            price += 3000

        if self.sport_interior == 'Y':
            price += 2000

        return price

class Luxury(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.gps = 'N'
        self.self_driving = 'N'

    def GPS(self):
        self.gps = 'Y'

    def SelfDriving(self):
        self.self_driving = 'Y'

    def pricewithoptions(self):
        price = self.discount_price()

        if self.gps == 'Y':
            price += 5000

        if self.self_driving == 'Y':
            price += 10000

        return price


# Test object
#car1 = Sport('BMW', 'M3', 60000)

#car1.SportWheels()
#car1.SportEngine()
#car1.SportInterior()

#print(car1.make())
#print(car1.model())
#print('Sticker Price:', car1.sticker_price())
#print('Discount Price:', car1.discount_price())
#print('Price With Options:', car1.pricewithoptions())


lux1 = Luxury('Tesla', 'Model S', 90000)

lux1.GPS()
lux1.SelfDriving()

print(lux1.make())
print(lux1.model())
print('Sticker Price:', lux1.sticker_price())
print('Discount Price:', lux1.discount_price())
print('Price With Options:', lux1.pricewithoptions())