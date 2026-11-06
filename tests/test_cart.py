import contextlib
import io
import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_discounted_total_and_invalid_percent(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            cart.add_dvd(DigitalVideoDisc("Example", cost=100))
        self.assertEqual(80, cart.total_cost_with_discount(20))
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_add_dvd_until_full(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            for index in range(MAX_NUMBERS_ORDERED):
                self.assertTrue(cart.add_dvd(DigitalVideoDisc(str(index))))
            self.assertFalse(cart.add_dvd(DigitalVideoDisc("extra")))
        self.assertEqual(MAX_NUMBERS_ORDERED, len(cart.items))


if __name__ == "__main__":
    unittest.main()
