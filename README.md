# Mini Kelime Tahmin Oyunu

Bu proje, kullanıcıların bir kelimeyi harf harf tahmin etmeye çalıştığı basit bir kelime tahmin oyunudur. Kelime listesi bir API'den çekilir ve kullanıcıya rastgele bir kelime sunulur. Kullanıcı, belirli sayıda yanlış tahmin yapmadan kelimeyi doğru tahmin etmeye çalışır.

## Kurulum

Bu projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. Bu projeyi yerel makinenize klonlayın:
    ```sh
    git clone https://github.com/kullaniciadi/mini-kelime-tahmin-oyunu.git
    cd mini-kelime-tahmin-oyunu
    ```

2. Gerekli Python paketlerini yükleyin:
    ```sh
    pip install requests
    ```

## Kullanım

Oyunu başlatmak için aşağıdaki komutu çalıştırın:
```sh
python app.py
```

### Kod Açıklaması
app.py dosyası, oyunun ana mantığını içerir. İşte dosyanın temel yapısı:

* kelime_listesi_cek fonksiyonu, kelime listesini bir API'den çeker. Eğer API'den kelime listesi çekilemezse, varsayılan bir kelime listesi kullanılır.
* Rastgele bir kelime seçilir ve kullanıcıdan bu kelimeyi harf harf tahmin etmesi istenir.
* Kullanıcı her yanlış tahmin yaptığında, adam asmaca görseli güncellenir.
Kullanıcı doğru kelimeyi tahmin ederse, tebrik mesajı gösterilir. Yanlış tahmin hakkı biterse, oyun sona erer ve doğru kelime gösterilir.

### Katkıda Bulunma
Katkıda bulunmak isterseniz, lütfen bir pull request gönderin veya bir issue açın.
