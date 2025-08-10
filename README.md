# İngilizce-Türkçe Word Quiz Game [TR]
Python ve Tkinter kütüphanesi kullanılarak geliştirilmiş, İngilizce kelime öğrenmeye yönelik interaktif bir masaüstü uygulamasıdır. 
Öğrenme ve tekrar yapmak isteyen kullanıcılar için sade ve kullanışlı bir deneyim sunar.

---

## İçindekiler

- [Genel Bakış](#genel-bakış)  
- [Özellikler](#özellikler)  
- [Kurulum](#kurulum)  
- [Kullanım](#kullanım)  
- [Dosya Yapısı](#dosya-yapısı)
- [Lisans](#Lisans)
- [Not](#Not)

---

## Genel Bakış

Genel Bakış
Bu proje, Python ve Tkinter kütüphanesi kullanılarak geliştirilmiş, İngilizce kelime öğrenmeye yönelik interaktif bir masaüstü uygulamasıdır. 
Kullanıcıya rastgele seçilen İngilizce kelimeler gösterilir ve doğru Türkçe karşılığını girmesi istenir. 
Basit ve anlaşılır arayüzü sayesinde her yaş grubundan kullanıcı kolayca oynayabilir.

Uygulama, esnek yapısı sayesinde gelecekte CSV dosyalarından kelime listesi okuma özelliğine sahip olacak, böylece kullanıcı kendi kelime havuzunu oluşturabilecektir. 
Ayrıca, Türkçe → İngilizce oyun modu, kullanıcı hesapları, skor kaydı, farklı zorluk seviyeleri ve gelişmiş arayüz tasarımları gibi ek özellikler planlanmaktadır.  

Proje şu anda geliştirme aşamasında olup, yeni sürümlerde daha zengin içerik ve kişiselleştirme seçenekleri sunmayı hedeflemektedir.

---

## Özellikler

### Mevcut Özellikler
- `Tkinter` tabanlı **kullanıcı dostu arayüz**
- **İngilizce → Türkçe** kelime çeviri modu
- **Rastgele kelime seçimi** ile her oyun için farklı sorular
- **Doğru / yanlış cevap takibi** ve skor gösterimi
- **Oyun bitiş ekranı** ile sonuç özeti

### Planlanan Özellikler
- **CSV dosyasından kelime listesi okuma** desteği (kendi kelime havuzunu oluşturma)
- **Türkçe → İngilizce** çeviri modu
- **Kullanıcı hesabı ve skor kaydı** sistemi
- **Farklı zorluk seviyeleri** (kolay, orta, zor)
- **Zenginleştirilmiş arayüz tasarımı** ve ek ekranlar
- **Ses efektleri ve animasyonlar** ile etkileşimli deneyim
- **İstatistik ve ilerleme takibi** özelliği
- **Kişiselleştirme seçenekleri** (tema, renk, font vb.)

---

## Kurulum

1. **Depoyu Klonlayın**  
git clone https://github.com/berkdnmz/English-word-quiz-GUI.git
cd English-word-quiz-GUI


2. **Python Sürümünü Kontrol Edin**  
Projenin çalışması için **Python 3.10 veya üzeri** gereklidir.  
python --version  


3. **Gereksinimleri Kurun**  
`tkinter` çoğu Python kurulumunda yüklü gelir. Ek kütüphaneler varsa `requirements.txt` dosyasından yükleyebilirsiniz.  
pip install -r requirements.txt  


4. **Oyunu Başlatın**  
python main.py  

---
## Kullanım

Terminal veya komut satırında projenin bulunduğu dizinde:

```bash
python main.py
```

1. Uygulamayı başlattıktan sonra **START** butonuna tıklayın.

2. Ekranda beliren İngilizce kelimenin Türkçe karşılığını ilgili kutucuğa yazın ve **Enter** tuşuna basın.

3. Doğru cevapsa **CORRECT!**, yanlışsa doğru cevap ekranda gösterilecektir.

4. Her cevap sonrası yeni kelime otomatik olarak gösterilir.

5. Oyun sonunda toplam doğru ve yanlış sayıları ekranda görüntülenir.

6. Oyundan çıkmak için **Escape (Esc)** tuşuna basabilirsiniz.

### İlerleyen sürümlerde;  
- Farklı oyun modları (Türkçe → İngilizce),  
- Skor kaydı ve kullanıcı profilleri,  
- Kişiselleştirme seçenekleri eklenecektir.


---

## Dosya Yapısı

```
English-word-quiz-GUI/
│
├── main.py          # Uygulamanın ana çalıştırma dosyası
├── game.py          # Oyun mantığı ve akışı
├── gui.py           # Arayüz tasarımı ve olay yönetimi
├── word_manager.py  # Kelime veri yönetimi
├── LICENSE          # Lisans dosyası
└── README.md        # Proje dökümantasyonu
```
---
## Not
> **Not:**  
> Bu proje daha önce CLI (Komut Satırı) versiyonu olarak geliştirilmiştir.  
> CLI versiyonunu incelemek için buraya bakabilirsiniz:  
> [CLI Versiyonu GitHub’da](https://github.com/berkdnmz/English-Quiz-CLI)  
>  
> Bu depo ise Tkinter ile geliştirilmiş yeni GUI versiyonudur.

---
## Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak sunulmuştur.  
Dilediğiniz gibi kullanabilir, değiştirebilir ve paylaşabilirsiniz — ancak orijinal geliştiriciyi belirtmeniz gerekir.

---

## Proje Sahibi

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Projeyle ilgili her türlü soru ve öneri için bana ulaşabilirsiniz.  



**İyi çalışmalar ve bol kelime öğrenmeli oyunlar!**