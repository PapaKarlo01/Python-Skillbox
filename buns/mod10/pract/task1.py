import re
import doctest


def check_password(password: str) -> bool:
    """Функция проверяет корректность пароля

    Args:
          password (str): Пароль, который необходимо проверить

    Returns:
          bool: True/False - корректен ли пароль

    >>> check_password('rtG3FG!Tr^e')
    True

    >>> check_password('aA1!*!1Aa')
    True

    >>> check_password('oF^a1D@y5e6')
    True

    >>> check_password('enroi#$rkdeR#$092uWedchf34tguv394h')
    True

    >>> check_password('пароль')
    False

    >>> check_password('password')
    False

    >>> check_password('qwerty')
    False

    check_password('lOngPa$$$W0Rd')
    False
    """
    if re.fullmatch(r'[a-z(A-Z{2,})(0-9+)^$%@#&*!?{2,}]{6,}', password) is None: return False
    return True

doctest.testmod()
