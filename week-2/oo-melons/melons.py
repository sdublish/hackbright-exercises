"""Classes for melon orders."""
from random import randint
from datetime import date, datetime


class TooManyMelonsError(ValueError):
    def __init__(self, message):
        super().__init__(message)


class AbstractMelonOrder():
    shipped = False
    date_placed = date.today().weekday()  # integer value (0:Mon, 6:sun)
    time_placed = datetime.now().hour

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.species = species

        if qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")

        self.qty = qty

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        return total

    def get_base_price(self):
        base_price = randint(5, 9)

        if (0 <= self.date_placed <= 4) and (8 <= time_placed <= 11):
            base_price += 4

        return base_price


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):
        international_total = super().get_total()

        if self.qty < 10:
            international_total += 3

        return international_total


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0.0
    passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed



