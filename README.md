# patolojises
# Türkçe Patoloji Rapor Dikte Sistemi

Bu proje, Türkçe patoloji raporlarının makroskopik, mikroskopik ve genel rapor formatlarında dikte edilerek raporlanmasını sağlar. Proje, ses kayıtlarının ve transkriptlerinin yönetimi için bir Tkinter GUI uygulaması için ses kütüphanesi oluşturmak.

## Katılım Şartları

Projeye katılmak için aşağıdaki şartları yerine getirmeniz gerekmektedir:
- Python programlama dilinde temel bilgiye sahip olmak.
- Git ve GitHub hakkında temel bilgiye sahip olmak.
- İki karakterlik benzersiz bir kullanıcı adı belirlemek.
- Ses dosyası ve buna karşılık gelen düz yazı txt dosyasını yüklemelisiniz. Bunlar yüzlerce ve binlerce olduğunda ses kütüphanesi faydalı olabilecektir.
- Oluşmakta olan ses kütüphanesi yapay zeka ses tanıma, sesi tıbbi patoloji formatında yazıya geçirme eğitiminde kullanılacaktır.

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

1. gui_app.py  Python dosyası: ses kaydı ve karşılığı txt dosyası oluşturur.  
kullanıcı adını bir kez belirleyip daha sonra yapılandırma dosyasından okuyacak ve klasör yapısını oluşturacaktır. ses dosyası ve karşılığı txt dosyalarını gui_app.py dizininde düzgün dosya sistemi ile oluşturacaktır.

2. upload_to_github.py Python dosyası: oluşturulmuş ses karşılığı txt dosyalarını github kendi klasörünüze otomatik yükler

### Kullanıcı Rehberi ve Bilgilendirme

1. **README.md**: Kullanıcıların projeye nasıl katılacağını ve projeyi nasıl kullanacağını açıkça belirtir.
2. **CONTRIBUTING.md**: Projeye katkıda bulunmak isteyenler için adımları ve kuralları içerir.
3. **.gitignore**: Gereksiz dosyaların Git deposuna eklenmesini önler.

### Projeyi Paylaşma

1. **GitHub Deposu Oluşturma**: GitHub'da yeni bir depo oluşturun ve proje dosyalarını bu depoya yükleyin.
2. **Proje Dosyalarını Yükleme**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/kullaniciadi/depoadi.git
   git push -u origin main
   ```

### Sonuç

Bu adımlar ve dosyalar, projenize katılmak isteyenler için kapsamlı bir rehber sunar. Katılımcılar gerekli kurulumları yapabilir, projeyi klonlayabilir, kullanıcı adı belirleyebilir ve ses kayıtlarını yönetebilir. Ayrıca, katkıda bulunmak isteyenler için yol gösterici bir rehberdir.
