# Library Management System

## Proje Özeti

Bu proje, Python ve SQLite kullanılarak geliştirilmiş bir Kütüphane Yönetim Sistemi'dir. Sistem; kitapların, üyelerin ve ödünç alma işlemlerinin yönetilmesini sağlamaktadır. Kullanıcılar komut satırı arayüzü (CLI) üzerinden kitap ekleme, listeleme, güncelleme, silme, üye işlemleri ve ödünç alma işlemlerini gerçekleştirebilmektedir.

Tüm veriler SQLite veritabanında saklanmakta olup tablolar arasında yabancı anahtar (Foreign Key) ilişkileri kurulmuştur.

---

## Kullanılan Teknolojiler

* Python 3
* SQLite3
* Git
* GitHub
* unittest

---

## Proje Yapısı

```text
library-management-system/
│
├── database/
│   ├── schema.sql
│   └── sample_data.sql
│
├── src/
│   ├── database.py
│   ├── book.py
│   ├── member.py
│   ├── loan.py
│   └── main.py
│
├── tests/
│   └── test_system.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Veritabanı Tasarımı

Proje üç temel tablodan oluşmaktadır:

### Books

Kitap bilgilerini saklar.

Alanlar:

* id
* title
* author
* year

### Members

Üye bilgilerini saklar.

Alanlar:

* id
* name
* email

### Loans

Ödünç alma kayıtlarını saklar.

Alanlar:

* id
* book_id
* member_id
* loan_date
* return_date

Loans tablosu, Books ve Members tablolarına Foreign Key ile bağlıdır.

---

## Özellikler

### Kitap İşlemleri

* Kitap ekleme
* Kitap listeleme
* Kitap güncelleme
* Kitap silme
* Kitap arama

### Üye İşlemleri

* Üye ekleme
* Üye listeleme
* Üye güncelleme
* Üye silme
* Üye arama

### Ödünç İşlemleri

* Kitap ödünç verme
* Aktif ödünçleri görüntüleme
* Kitap iade etme
* Ödünç geçmişini görüntüleme

---

## Kurulum

Projeyi klonlayın:

```bash
git clone https://github.com/mthnsnl/library-management-system.git
```

Proje klasörüne girin:

```bash
cd library-management-system
```

Programı çalıştırın:

```bash
python src/main.py
```

---

## Testler

Proje Python'un unittest modülü kullanılarak test edilmiştir.

Test edilen bileşenler:

* Veritabanı bağlantısı
* Kitap ekleme işlemleri
* Üye ekleme işlemleri
* Ödünç verme işlemleri

Testleri çalıştırmak için:

```bash
python tests/test_system.py
```

---

## Geliştirme Süreci

Proje geliştirilirken öncelikle veritabanı tasarımı yapılmıştır. Books, Members ve Loans tabloları oluşturulmuş ve tablolar arasındaki ilişkiler belirlenmiştir.

Daha sonra Python kullanılarak SQLite veritabanına bağlantı kurulmuş ve kitap işlemleri için CRUD fonksiyonları geliştirilmiştir. Aynı süreç üye yönetimi için de uygulanmıştır.

Sonraki aşamada ödünç alma sistemi geliştirilmiş, kitapların ödünç verilmesi ve iade edilmesi işlemleri eklenmiştir. Ardından komut satırı arayüzü geliştirilerek sistem kullanıcı dostu hale getirilmiştir.

Son olarak test senaryoları hazırlanmış ve GitHub üzerinde sürüm kontrolü sağlanmıştır.

---

## Karşılaşılan Zorluklar

Proje sırasında özellikle aşağıdaki konularda zorluk yaşanmıştır:

* SQL tabloları arasında ilişki kurulması
* Foreign Key yapısının doğru tasarlanması
* Ödünç verilmiş kitapların tekrar ödünç alınmasının engellenmesi
* CRUD işlemlerinin modüler şekilde geliştirilmesi
* GitHub üzerinde düzenli commit geçmişi oluşturulması

Bu zorluklar araştırma yapılarak ve uygulamalar geliştirilerek aşılmıştır.

---

## Öğrendiklerim

Bu proje sayesinde aşağıdaki konularda deneyim kazanılmıştır:

* Python ile veritabanı programlama
* SQLite kullanımı
* SQL sorguları yazma
* CRUD operasyonları geliştirme
* Foreign Key ilişkileri oluşturma
* Komut satırı arayüzü geliştirme
* Yazılım projelerinde modüler yapı kurma
* Git ve GitHub ile sürüm kontrolü

---

## Python'ın Rolü

Python, uygulamanın temel programlama dili olarak kullanılmıştır. Kullanıcıdan alınan verilerin işlenmesi, veritabanı işlemlerinin gerçekleştirilmesi ve sistem mantığının oluşturulması Python ile sağlanmıştır.

---

## SQL'in Rolü

SQL, verilerin saklanması ve yönetilmesi amacıyla kullanılmıştır. Veritabanı tabloları SQL komutları ile oluşturulmuş ve CRUD işlemleri SQL sorguları aracılığıyla gerçekleştirilmiştir.

---

## Git ve GitHub'ın Rolü

Git, proje süresince sürüm kontrol sistemi olarak kullanılmıştır. Yapılan değişiklikler düzenli commit'lerle kayıt altına alınmıştır.

GitHub ise projenin çevrimiçi olarak saklanmasını, yedeklenmesini ve geliştirme sürecinin takip edilmesini sağlamıştır. Commit geçmişi sayesinde projenin hangi aşamalardan geçtiği açık şekilde görülebilmektedir.

---

## Sonuç

Bu proje kapsamında Python ve SQLite kullanılarak işlevsel bir Kütüphane Yönetim Sistemi geliştirilmiştir. Sistem, kitap yönetimi, üye yönetimi ve ödünç alma işlemlerini desteklemektedir. Ayrıca Git ve GitHub kullanılarak sürüm kontrolü uygulanmış ve yazılım geliştirme süreci düzenli şekilde yönetilmiştir.
