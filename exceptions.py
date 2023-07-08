class InvalidInputException(Exception):
    """Raised for invalid input"""


class InvalidRowsException(InvalidInputException):
    """Raised if the number of rows is invalid"""


class InvalidLevelException(InvalidInputException):
    """Raised if the header level is invalid"""
