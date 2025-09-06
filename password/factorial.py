def factorial(n):
    try:
        n = int(n)
    except:
        return "Lütfen sayı giriniz."
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Hesaplanamaz."
    sonuc = 1
    for i in range(1, n+1):
        sonuc = sonuc * i
    return sonuc

if __name__ == "__main__":
    print(factorial("a"))