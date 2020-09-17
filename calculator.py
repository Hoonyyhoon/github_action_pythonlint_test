# -*- coding: utf-8 -*-
"""Integer calcualtor with basic operators.

- Auther: Junghoon Kim
- Contact: jhkim@jmarple.ai

"""


class Calculator:
    """Abstract calculator which works as an interface."""

    def operate(self, x, y):
        """Abstract method that is inherited by specific operators.

        Args:
            x (int) : left operand
            y (int) : right operand

        Return:
            int: operation result
        """
        pass


class Adder(Calculator):
    """Add operation."""

    def operate(self, x, y):
        """Operate add."""
        pass


class Subtractor(Calculator):
    """Subtract operation."""

    def operate(self, x, y):
        """Operate subtract."""
        pass


class Multiplier(Calculator):
    """Multiplier operation."""

    def operate(self, x, y):
        """Operate multiply."""
        pass


class Divider(Calculator):
    """Divider operation."""

    def operate(self, x, y):
        """Operate divide."""
        pass
