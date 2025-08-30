from password.factorial import factorial

def test_factorial():
    x = factorial(5)
    assert x == 120

def test_factorial_withletter():
    x = factorial("a")
    assert x == "Lütfen sayı giriniz."