from Main import input_ready


def calc(expression):
    try:
        value = input_ready(expression)
        return value
    except Exception:
        return "Invalid"


def test_calculator():
    assert calc("5+6/2/") == "Invalid"
    assert calc("((5-6*4)-5") == "Invalid"
    assert calc("4-+3%4") == "Invalid"
    assert calc("$20-60$2") == "Invalid"
    assert calc("!4--5!") == "Invalid"
    assert calc("jgv7459jg") == "Invalid"
    assert calc("") == "Invalid"
    assert calc("       ") == "Invalid"

    assert calc("2+3") == 5
    assert calc("8-4") == 4
    assert calc("5*7") == 35
    assert calc("20/4") == 5.0
    assert calc("3^2") == 9
    assert calc("16%3") == 1
    assert calc("10@15") == 12.5
    assert calc("40$30") == 40
    assert calc("25&30") == 25
    assert calc("~9") == -9
    assert calc("-6") == -6
    assert calc("4!") == 24
    assert calc("12#") == 3
    assert calc("~5*2") == -10
    assert calc("7-2!") == 5

    assert calc("(5+3) * 2 - 4") == 12
    assert calc("10 / (2^2) + 1") == 3.5
    assert calc("~(8 + 2) * 3") == -30
    assert calc("6$((3*2)-4) + 5") == 11
    assert calc("2^3 * 4 - 10") == 22
    assert calc("15 & ~(4-1) * 2") == -6
    assert calc("25@5 + (12%3)") == 15
    assert calc("(10 - 3) ^ 2 + 1") == 50
    assert calc("9/3 + ~2 + 5") == 6.0
    assert calc("(8*2) - (6+1)!") == -5024
    assert calc("(~4 + 3^2) * 2") == 10
    assert calc("18 * (5 - 2!) + 1") == 55
    assert calc("5 + (3^2) @ 2 - 1") == 9.5
    assert calc("(~2) * 4^2 + 10") == -22
    assert calc("10! / 5 + (3 * 2)") == 725766
    assert calc("7$5 + ~(3-1) ^ 2") == 11
    assert calc("20 - (4*2) @ (6/3)") == 15
    assert calc("((2+3) * 4) ^ 2") == 400
    assert calc("7 - 2! / (3^2) + 1") == 7.777777777777778
    assert calc("20$5 + ~(4-2) ^ 3") == 12


