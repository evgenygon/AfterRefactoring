import unittest

from dealership.vehicles import Car, Truck, Motorcycle


class CarTestCase(unittest.TestCase):
    a = Car(maker='Ford', model='Mustang', year=2005, base_price=18000, miles=31000) #example object
    b = Car(maker='Ford', model='Mustang', year=2014, base_price=31000, miles=11000) #example object

    def is_it_maker_equal_to_FORD(self):
        self.assertEquals(CarTestCase.a.maker, 'Ford')

    def test_car_creation(self):
        self.assertEqual(CarTestCase.a.maker, 'Ford')
        self.assertEqual(CarTestCase.a.model, 'Mustang')
        self.assertEqual(CarTestCase.a.year, 2005)
        self.assertEqual(CarTestCase.a.base_price, 18000)
        self.assertEqual(CarTestCase.a.miles, 31000)

    def test_cars_sale_price(self):
        self.assertEqual(CarTestCase.a.sale_price(), 21600)
        self.assertEqual(CarTestCase.b.sale_price(), 37200)

    def test_cars_purchase_price(self):

        self.assertEqual(CarTestCase.a.purchase_price(), 21476)
        self.assertEqual(CarTestCase.b.purchase_price(), 37156)


class TruckTestCase(unittest.TestCase):
    c = Truck(maker='Chevrolet', model='Silverado', year=2014, base_price=29000, miles=3000) #example object
    d = Truck(maker='Chevrolet', model='Silverado', year=2004, base_price=16000, miles=52000) #example object

    def test_truck_creation(self):
        self.assertEqual(TruckTestCase.c.maker, 'Chevrolet')
        self.assertEqual(TruckTestCase.c.model, 'Silverado')
        self.assertEqual(TruckTestCase.c.year, 2014)
        self.assertEqual(TruckTestCase.c.base_price, 29000)
        self.assertEqual(TruckTestCase.c.miles, 3000)

    def test_trucks_sale_price(self):
        self.assertEqual(TruckTestCase.c.sale_price(), 46400)
        self.assertEqual(TruckTestCase.d.sale_price(), 25600)

    def test_trucks_purchase_price(self):
        self.assertEqual(TruckTestCase.c.purchase_price(), 46340)
        self.assertEqual(TruckTestCase.d.purchase_price(), 24560)


class MotorcycleTestCase(unittest.TestCase):
    e = Motorcycle(maker='Ducati', model='Monster', year=2016, base_price=18000, miles=700) #example object
    f = Motorcycle(maker='Ducati', model='Monster', year=2009, base_price=9000, miles=11400) #example object
    def test_motorcycle_creation(self):
        self.assertEqual(MotorcycleTestCase.e.maker, 'Ducati')
        self.assertEqual(MotorcycleTestCase.e.model, 'Monster')
        self.assertEqual(MotorcycleTestCase.e.year, 2016)
        self.assertEqual(MotorcycleTestCase.e.base_price, 18000)
        self.assertEqual(MotorcycleTestCase.e.miles, 700)

    def test_motorcycle_sale_price(self):
        self.assertEqual(MotorcycleTestCase.e.sale_price(), 19800)
        self.assertEqual(MotorcycleTestCase.f.sale_price(), 9900)

    def test_motorcycle_purchase_price(self):
        self.assertEqual(MotorcycleTestCase.e.purchase_price(), 19793.7)
        self.assertEqual(MotorcycleTestCase.f.purchase_price(), 9797.4)
