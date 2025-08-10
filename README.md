# English-Turkish Word Quiz Game
An interactive desktop application developed using Python and the Tkinter library to help users learn English vocabulary.
It offers a simple and user-friendly experience for learners who want to study and review.
---
## Table of Contents

- [English Section](#english-turkish-word-quiz-game)
- [Türkçe Bölüm](#ingilizce-türkçe-word-quiz-game-tr)
---
## Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [File Structure](#file-structure)  
- [License](#license)  
- [Note](#note)
---
## Overview

This project is an interactive desktop application developed using Python and the Tkinter library to help users learn English vocabulary.  
Randomly selected English words are shown to the user, who is then asked to enter the correct Turkish translation.  
Thanks to its simple and clear interface, users of all ages can easily play.

Due to its flexible structure, the application will support reading word lists from CSV files in the future, allowing users to create their own word pools.  
Additionally, features such as a Turkish → English game mode, user accounts, score tracking, different difficulty levels, and enhanced UI designs are planned.

The project is currently under development and aims to offer richer content and personalization options in upcoming releases.

---
## Features

### Current Features
- User-friendly interface based on `Tkinter`
- English → Turkish translation game mode
- Random word selection for varied questions each game
- Correct / incorrect answer tracking and score display
- End-game screen with summary

### Planned Features
- Support for reading word lists from CSV files (creating custom word pools)
- Turkish → English translation mode
- User account and score saving system
- Different difficulty levels (easy, medium, hard)
- Enhanced UI design and additional screens
- Interactive experience with sound effects and animations
- Statistics and progress tracking
- Personalization options (theme, color, font, etc.)

---
## Installation

1. **Clone the repository**  
git clone https://github.com/berkdnmz/English-word-quiz-GUI.git  
cd English-word-quiz-GUI


2. **Check Python version**  
Python 3.10 or higher is required to run the project.  
python --version  


3. **Install dependencies**  
`tkinter` usually comes pre-installed with Python. If there are additional packages, you can install them from the `requirements.txt` file.  
pip install -r requirements.txt  


4. **Start the game**  
python main.py  

---
## Usage

In the terminal or command prompt, navigate to the project directory and run:

```bash
python main.py
```
1. After launching the application, click the **START** button.

2. Type the Turkish translation of the English word displayed on the screen into the input box and press **Enter**.

3. If the answer is correct, **CORRECT!** will be shown; if wrong, the correct answer will be displayed.

4. After each answer, a new word will automatically appear.

5. At the end of the game, the total number of correct and incorrect answers will be shown on the screen.

6. To exit the game, press the **Escape (Esc)** key.

### In future versions;  
- Different game modes (Turkish → English),  
- Score saving and user profiles,  
- Personalization options will be added.

---
## File Structure
```
English-word-quiz-GUI/
│
├── main.py          # Main application entry point
├── game.py          # Game logic and flow
├── gui.py           # Interface design and event handling
├── word_manager.py  # Word data management
├── LICENSE          # License file
└── README.md        # Project documentation
```
---
## Note
> **Note:**  
> This project was previously developed as a CLI (Command Line Interface) version.  
> You can check out the CLI version here:  
> [CLI Version on GitHub](https://github.com/berkdnmz/English-Quiz-CLI)  
>  
> This repository is the new GUI version developed with Tkinter.
---
## License

This project is open source under the [MIT License](LICENSE).  
You are free to use, modify, and distribute it as you wish — however, you must credit the original author.

---
## Project Owner

**Berk DÖNMEZ**

GitHub: [github.com/berkdnmz](https://github.com/berkdnmz)  
LinkedIn: [linkedin.com/in/berkdnmz](https://linkedin.com/in/berkdnmz)  

Feel free to contact me for any questions or suggestions regarding the project.

**Happy coding and enjoy learning lots of new words!**

---

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
