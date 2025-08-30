import random
import string

def generate_password(length=12):
    """Belirtilen uzunlukta rastgele bir şifre oluşturur."""
    try:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''
        for i in range(length):
            password += random.choice(characters)
            if i % 100 == 0:
                print(f"{i} tur geçti")
        return password
    except:
        password = "Başaramadın"

# Kullanım örneği
password_length = 12  # İstediğiniz herhangi bir şifre uzunluğunu seçebilirsiniz
print("Yeni şifreniz:", generate_password(password_length))
