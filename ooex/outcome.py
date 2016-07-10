# -*- coding: utf-8 -*-

class Outcome():
    """The outcome of roulette."""

    def __init__(self, name, odds):
        """Initialize an outcome

        Args:
            name (str): the name of an outcome (e.g., red)
            odds (int): odds for the outcome (e.g., 9 for 9:1)
        """
        self.name = name
        self.odds = odds

    def __str__(self):
        """Print string representation of outcome

        Returns:
            str: string like "red (2:1)"

        """
        return "{} ({}:1)".format(self.name, self.odds)

    def winAmount(self, amount):
        """What dollar amount is won with this outcome?

        Args:
            amount (float): what dollar amount was bet?

        Returns:
            float: product of the amount bet and the odds
        """
        return self.odds * amount

    def __eq__(self, other):
        """Equality test for two outcomes

        Args:
            other (Outcome): outcome to compare for equality

        Returns:
            bool: Do the two bets have the same name?

        """
        return str(self.name) == str(other.name)

    def __ne__(self, other):
        """Inequality test for two outcomes

        Args:
            other (Outcome): outcome to compare for inequality

        Returns:
            bool: Do the two bets have different names?

        """
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)
