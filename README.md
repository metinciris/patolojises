# patolojises
# Türkçe Patoloji Rapor Dikte Sistemi

Bu proje, Türkçe patoloji raporlarının makroskopik, mikroskopik ve genel rapor formatlarında dikte edilerek raporlanmasını sağlar. Proje, ses kayıtlarının ve transkriptlerinin yönetimi için bir Tkinter GUI uygulamasıdır.

## Katılım Şartları

Projeye katılmak için aşağıdaki şartları yerine getirmeniz gerekmektedir:
- Python programlama dilinde temel bilgiye sahip olmak.
- Git ve GitHub hakkında temel bilgiye sahip olmak.
- İki karakterlik benzersiz bir kullanıcı adı belirlemek.

## Gerekli Kurulumlar

Projeye katılmak ve geliştirme ortamınızı hazırlamak için aşağıdaki adımları izleyin:

### 1. Python Kurulumu
Python 3.8 veya daha yeni bir sürümünü kurun. Python'u [resmi web sitesinden](https://www.python.org/downloads/) indirebilirsiniz.

### 2. Gerekli Python Kütüphanelerinin Kurulumu
Gerekli kütüphaneleri kurmak için aşağıdaki komutu çalıştırın:
```bash
pip install sounddevice wavio
```

### 3. Git ve GitHub Kurulumu
GitHub hesabı oluşturun ve Git'i bilgisayarınıza kurun. Git'i [resmi web sitesinden](https://git-scm.com/) indirebilirsiniz.

### 4. Projeyi Klonlama
Projeyi bilgisayarınıza klonlamak için aşağıdaki komutu çalıştırın:
```bash
git clone https://github.com/kullaniciadi/depoadi.git
cd depoadi
```

### 5. Kullanıcı Adınızı Belirleme
Projeyi ilk kez çalıştırdığınızda, iki karakterlik benzersiz bir kullanıcı adı belirlemeniz istenecektir. Bu kullanıcı adı, tüm dosya isimlerinizde ve klasörlerinizde kullanılacaktır.

## Kullanım

Projeyi başlatmak için aşağıdaki komutu çalıştırın:
```bash
python gui_app.py
```

### Ses Kaydı Yapma
- "Start Recording" düğmesine tıklayarak kayıt başlatılır.
- "Stop Recording" düğmesine tıklayarak kayıt durdurulur ve dosya kaydedilir.

### Transkripsiyon Ekleme
Kayıt tamamlandığında, kullanıcıdan transkript metni istenir ve ilgili klasöre kaydedilir.

### Gönderilmemiş Dosyaları Listeleme
"List Unsent Files" düğmesine tıklayarak gönderilmemiş dosyalar listelenir.

### Dosya Silme
"Delete File" düğmesine tıklayarak bir dosya silinebilir. Kullanıcıdan silinecek dosya ismi istenir.

### Bulut Klasöründen İçe Aktarma
"Import from Cloud" düğmesine tıklayarak bulut klasöründen dosyalar içe aktarılabilir. Dosyalar kullanıcı klasörlerine uygun şekilde yerleştirilir.

## Örnek Raporlar

Projede, makroskopik, mikroskopik ve genel rapor formatlarında örnek rapor metinleri de saklanabilir. Kullanıcılar kendi klasörlerinde `example_reports` adlı bir klasör oluşturup bu örnek rapor metinlerini buraya yükleyebilirler.

## Katkıda Bulunma

Katkıda bulunmak isterseniz aşağıdaki adımları izleyin:
1. Projeyi forklayın.
2. Yeni bir özellik veya düzeltme için bir branch oluşturun:
   ```bash
   git checkout -b yeni-ozellik
   ```
3. Yaptığınız değişiklikleri commitleyin:
   ```bash
   git add .
   git commit -m "Yeni özellik eklendi"
   ```
4. Branch'i GitHub'a push edin:
   ```bash
   git push origin yeni-ozellik
   ```
5. Bir pull request açın.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
```

### CONTRIBUTING.md Dosyası

```markdown
# Katkıda Bulunma Rehberi

Bu projeye katkıda bulunmak için aşağıdaki adımları izleyin:

## Fork ve Branch

1. Projeyi forklayın.
2. Yeni bir branch oluşturun:
   ```bash
   git checkout -b yeni-ozellik
   ```

## Değişiklik Yapma

3. Gerekli değişiklikleri yapın ve değişikliklerinizi commitleyin:
   ```bash
   git add .
   git commit -m "Yeni özellik eklendi"
   ```

## Pull Request Açma

4. Değişikliklerinizi GitHub'a push edin:
   ```bash
   git push origin yeni-ozellik
   ```

5. GitHub'da bir pull request açın.

## Kodlama Standartları

- Python kodları için PEP 8 standartlarına uyun.
- Anlaşılır ve açıklayıcı commit mesajları kullanın.
```

### .gitignore Dosyası

```gitignore
# Python
*.pyc
__pycache__/

# Ses dosyaları ve transkriptler
project/*/audio_files/
project/*/transcriptions/

# Yapılandırma dosyaları
config.txt
log.txt
```

### Proje Klasör Yapısı ve Dosyalar

Proje klasör yapısını yukarıda belirttiğimiz gibi oluşturun. Her katılımcının kendi klasöründe ses dosyaları (`audio_files`), transkriptler (`transcriptions`) ve örnek raporlar (`example_reports`) klasörleri olacaktır. `gui_app.py` dosyasını ve diğer yapılandırma dosyalarını projeye ekleyin.

### Python Kodunun Güncellenmesi

Aşağıdaki Python kodu, kullanıcı adını bir kez belirleyip daha sonra yapılandırma dosyasından okuyacak ve klasör yapısını oluşturacaktır.

```python
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import sounddevice as sd
import wavio
import os
import numpy as np
import threading

# Ses kaydı için ayarlar
samplerate = 16000  # Örnekleme hızı
project_folder = "project"
config_file = "config.txt"
log_file = "log.txt"

# Kullanıcı adını kontrol et ve yapılandırma dosyasına kaydet
if not os.path.exists(config_file):
    user_id = simpledialog.askstring("Input", "Enter your user ID (2 characters):")
    if len(user_id) != 2:
        raise ValueError("User ID must be exactly 2 characters long")
    with open(config_file, "w") as f:
        f.write(user_id)
else:
    with open(config_file, "r") as f:
        user_id = f.read().strip()

# Kullanıcı klasörünü oluşturma
user_folder = os.path.join(project_folder, user_id)
audio_folder = os.path.join(user_folder, "audio_files")
transcription_folder = os.path.join(user_folder, "transcriptions")
example_reports_folder = os.path.join(user_folder, "example_reports")
os.makedirs(audio_folder, exist_ok=True)
os.makedirs(transcription_folder, exist_ok=True)
os.makedirs(example_reports_folder, exist_ok=True)

# Mevcut en yüksek dosya numarasını bulun
def get_next_file_number():
    files = os.listdir(audio_folder)
    if not files:
        return 1
    numbers = [int(f.split(".")[0].split("_")[1]) for f in files if f.endswith(".wav")]
    return max(numbers) + 1 if numbers else 1

next_file_number = get_next_file_number()
is_recording = False
audio_data = []

def start_recording():
    global is_recording, audio_data
    if not is_recording:
        is_recording = True
        audio_data = []
        threading.Thread(target=record_audio).start()

def record_audio():
    global audio_data
    with sd.InputStream(samplerate=samplerate, channels
