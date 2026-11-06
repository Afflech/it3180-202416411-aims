import contextlib
import io
import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class CartTests(unittest.TestCase):
    def test_sort_by_title_and_cost(self):
        cart = Cart()
        with contextlib.redirect_stdout(io.StringIO()):
            cart.add_dvd(DigitalVideoDisc("Zebra", cost=5))
            cart.add_dvd(DigitalVideoDisc("apple", cost=10))
        cart.sort_by_title()
        self.assertEqual(["apple", "Zebra"], [dvd.title for dvd in cart.items])
        cart.sort_by_cost()
        self.assertEqual(["Zebra", "apple"], [dvd.title for dvd in cart.items])

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
