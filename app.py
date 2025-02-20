import random
import requests


def kelime_listesi_cek():
    response = requests.get("https://api.datamuse.com/words?sp=????&max=10")

    if response.status_code == 200:
        kelimeler = [kelime["word"] for kelime in response.json()]
        return kelimeler
    else:
        print("Kelime listesi çekilemedi.")
        return []


kelime_listesi = kelime_listesi_cek()

if not kelime_listesi:
    print("Kelime listesi bulunamadı, varsayılan liste kullanılacak.")
    kelime_listesi = ["elma", "armut", "muz", "çilek", "kavun", "karpuz"]

# Rastgele bir kelime seç
rastgele_kelime = random.choice(kelime_listesi)
kelime_uzunlugu = len(rastgele_kelime)
tahmin_edilen_kelime = ["_"] * kelime_uzunlugu
tahmin_edilen_harfler = []
haklar = 6

adam_asmaca_gorselleri = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """,
]

print("Kelime Tahmin Oyununa Hoş Geldiniz!")
print(" ".join(tahmin_edilen_kelime))

while "_" in tahmin_edilen_kelime and haklar > 0:
    print(adam_asmaca_gorselleri[6 - haklar])
    tahmin = input("Bir harf tahmin edin: ").lower()

    if tahmin in tahmin_edilen_harfler:
        print("Bu harfi zaten tahmin ettiniz.")
        continue

    tahmin_edilen_harfler.append(tahmin)

    if tahmin in rastgele_kelime:
        for index, harf in enumerate(rastgele_kelime):
            if harf == tahmin:
                tahmin_edilen_kelime[index] = tahmin
        print("Doğru tahmin!")
    else:
        haklar -= 1
        print(f"Yanlış tahmin. Kalan haklarınız: {haklar}")

    print(" ".join(tahmin_edilen_kelime))

print(adam_asmaca_gorselleri[6 - haklar])
if "_" not in tahmin_edilen_kelime:
    print(f"Tebrikler! Kelimeyi buldunuz: {rastgele_kelime}")
else:
    print(f"Maalesef, hakkınız bitti. Kelime: {rastgele_kelime}")
