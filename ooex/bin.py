# -*- coding: utf-8 -*-

class Bin():
    """A roulette bin, containing a collection of outcomes"""

    def __init__(self, *outcomes):
        """Initialize a bin

        Args:
            outcomes: any number of Outcomes used to populate the bin
        """
        self.outcomes = frozenset(outcomes)

    def add(self, outcome):
        """Adds an outcome to the bin

        Args:
            outcome: the Outcome to add to the bin

        Returns:
            a new frozen set containing the new outcome

        """
        self.outcomes |= set([outcome])
        return self.outcomes

    def __str__(self):
        """Pretty string representation of a bin

        Returns:
            string like "[outcome, outcome, outcome, ...]"

        """
        return ', '.join(map(str,self.outcomes))
