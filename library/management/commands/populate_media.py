from django.core.management.base import BaseCommand
from companies.models import *
from curricula.models import *
from publishers.models import *
from educategories.models import *
from questions.models import *
from components.models import *
from tests.models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class Command(BaseCommand):

    def _data_crate(self):

        LearningLectureYoutube.objects.bulk_create([
            LearningLectureYoutube(id=10001, name='Küçük Sayılarla Sayma', desc='-', file='https://www.youtube.com/embed/4ikFklV5i8U'),
            LearningLectureYoutube(id=10002, name='Sıralı Sayma', desc='-', file='https://www.youtube.com/embed/6759W3Lb3_o'),
            LearningLectureYoutube(id=10003, name='Sayı Tablosu Oluşturma', desc='-', file='https://www.youtube.com/embed/o0OVkMfUnxU'),
            LearningLectureYoutube(id=10004, name='0 ile 120 Arasındaki Eksik Sayıları Bulma', desc='-', file='https://www.youtube.com/embed/LSrRp_8v3jE'),
            LearningLectureYoutube(id=10005, name='Şekillerle Sayma', desc='-', file='https://www.youtube.com/embed/flEkSAGNaUQ'),
            LearningLectureYoutube(id=10006, name='Nesneleri Sayma Alıştırması: Balinaları, Koçları ve Çiçekleri Sayalım!', desc='-', file='https://www.youtube.com/embed/2EeNJz26qnI'),
            LearningLectureYoutube(id=10007, name='Nesneleri Sayma Alıştırması: Köpekleri, Fareleri ve Kurabiyeleri Sayalım!', desc='-', file='https://www.youtube.com/embed/XnUVYQjs-B0'),
            LearningLectureYoutube(id=10008, name='10’a Kadar Olan Nesne Sayılarını Karşılaştırma', desc='-', file='https://www.youtube.com/embed/hZcLyak9CPU'),
            LearningLectureYoutube(id=10009, name='10’a Kadar Olan Sayıları Sayı Doğrusu Üzerinde Karşılaştırma', desc='-', file='https://www.youtube.com/embed/gB75q-sNpNk'),
            LearningLectureYoutube(id=10010, name='Kategorilere Göre Sayma', desc='-', file='https://www.youtube.com/embed/i0ORNHhicmM'),

            LearningLectureYoutube(id=10011, name='Toplama', desc='-', file='https://www.youtube.com/embed/LUvz_OB9-EU'),
            LearningLectureYoutube(id=10012, name='Çıkarma', desc='-', file='https://www.youtube.com/embed/lji7ebMQKnA'),
            LearningLectureYoutube(id=10013, name='5 Elde Etme', desc='-', file='https://www.youtube.com/embed/EFG5F01Wuzg'),
            LearningLectureYoutube(id=10014, name='Kutuları Doldurarak 10 Elde Etme', desc='-', file='https://www.youtube.com/embed/fWHx1Jx7ALU'),
            LearningLectureYoutube(id=10015, name='10 ile Toplama İşlemi', desc='-', file='https://www.youtube.com/embed/bb0T-mQH5Yo'),
            LearningLectureYoutube(id=10016, name='Toplama ve Çıkarma Alıştırması: Meyveleri Sayalım!', desc='-', file='https://www.youtube.com/embed/ECTwXLH9KP8'),
            LearningLectureYoutube(id=10017, name='10’a Kadar Olan Sayılarla Toplama ve Çıkarma İşlemi', desc='-', file='https://www.youtube.com/embed/HzNDwqb1Wqo'),
            LearningLectureYoutube(id=10018, name='Toplama ve Çıkarma Arasındaki İlişki', desc='-', file='https://www.youtube.com/embed/8zoIS9L-fZY'),
            LearningLectureYoutube(id=10019, name='10’a Kadar Olan Sayılarla Toplama Problemleri', desc='-', file='https://www.youtube.com/embed/4anpcL4ITLI'),
            LearningLectureYoutube(id=10020, name='10’a Kadar Olan Sayılarla Çıkarma Problemleri', desc='-', file='https://www.youtube.com/embed/PhZrRnh9uKA'),

            LearningLectureYoutube(id=10021, name='10’lu Sayıların Toplam Halinde Gösterilmesi', desc='-', file='https://www.youtube.com/embed/LMcm8a1uoCc'),
            LearningLectureYoutube(id=10022, name='10’lu Sayılarla Alıştırma: Partiye Kaç Maymun Gelmeli?', desc='-', file='https://www.youtube.com/embed/Mro2xaRtdIY'),
            LearningLectureYoutube(id=10023, name='Basamak Değeri', desc='-', file='https://www.youtube.com/embed/G6gZB9E-8Pc'),
            LearningLectureYoutube(id=10024, name='25 ile Basamak Değeri Alıştırması', desc='-', file='https://www.youtube.com/embed/yG8ybVgnJLA'),
            LearningLectureYoutube(id=10025, name='42 ile Basamak Değeri Alıştırması', desc='-', file='https://www.youtube.com/embed/6YhrYRId4N4'),
            LearningLectureYoutube(id=10026, name='Büyüktür ve Küçüktür Simgeleri', desc='-', file='https://www.youtube.com/embed/VDB76h3vU6U'),
            LearningLectureYoutube(id=10027, name='Karşılaştırma işaretlerinin bir daha gözden geçirilmesi - (pdf)', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10028, name='Bu derste video veya makale yok. - (no content)', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10029, name='Doğal Sayıları Karşılaştırma', desc='-', file='https://www.youtube.com/embed/hPUXyqlwfO0'),

            LearningLectureYoutube(id=10030, name='Toplama Alıştırması: 7 + 6', desc='-', file='https://www.youtube.com/embed/6ZGg8MY4QK0'),
            LearningLectureYoutube(id=10031, name='Toplama Alıştırması: 8 + 7', desc='-', file='https://www.youtube.com/embed/9rHxcHoRlj0'),
            LearningLectureYoutube(id=10032, name='Toplama Alıştırması: 5 + 3 + 6', desc='-', file='https://www.youtube.com/embed/q_Hlhu2OBVo'),
            LearningLectureYoutube(id=10033, name='Çıkarma Alıştırması: 14 - 6', desc='-', file='https://www.youtube.com/embed/1shOsjXCyJM'),
            LearningLectureYoutube(id=10034, name='Eşittir İşareti', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10035, name='Bu derste video veya makale yok.', desc='-', file='https://www.youtube.com/embed/HHKCDiTuTJU'),
            LearningLectureYoutube(id=10036, name='Toplama ve Çıkarma Alıştırması: Göl Canavarları ve Süper Kahramanlar ', desc='-', file='https://www.youtube.com/embed/96Yh_xGpBaw'),
            LearningLectureYoutube(id=10037, name='Toplama ve Çıkarma Alıştırması: Spor Salonundaki Goriller', desc='-', file='https://www.youtube.com/embed/P5KLjXodCm4'),
            LearningLectureYoutube(id=10038, name='Karşılaştırma Problemleri ', desc='-', file='https://www.youtube.com/embed/dVU33TRI41w'),
            LearningLectureYoutube(id=10039, name='Karşılaştırma Problemleri ', desc='-', file='https://www.youtube.com/embed/RGxu__o1P8A'),
            LearningLectureYoutube(id=10040, name='Toplama İşlemine Örnekler', desc='-', file='https://www.youtube.com/embed/yAN099YZ6N4'),

            LearningLectureYoutube(id=10041, name='Bir Sayıya 1 ve 10 Eklemek Arasındaki Fark ', desc='-', file='https://www.youtube.com/embed/saXROdKIMvo'),
            LearningLectureYoutube(id=10042, name='Onlukları Eklerken Basamak Değerini Anlama ', desc='-', file='https://www.youtube.com/embed/iX7I3rdOCkI'),
            LearningLectureYoutube(id=10043, name='Birlikleri Eklerken Basamak Değerini Anlama', desc='-', file='https://www.youtube.com/embed/darB8BZ-dZo'),
            LearningLectureYoutube(id=10044, name='1’leri ve 10’ları toplamaya ilişkin yönlendirmeli alıştırmalar - (pdf)', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10045, name='1 Çıkarmak ve 10 Çıkarmak Arasındaki Fark ', desc='-', file='https://www.youtube.com/embed/0suRQ3B61XI'),
            LearningLectureYoutube(id=10046, name='Birlikleri Çıkarırken Basamak Değerini Anlama ', desc='-', file='https://www.youtube.com/embed/tUSuA4DdVoU'),
            LearningLectureYoutube(id=10047, name='Onlukları Çıkarırken Basamak Değerini Anlama', desc='-', file='https://www.youtube.com/embed/kqDAGp4HF54'),
            LearningLectureYoutube(id=10048, name='İki Basamaklı Sayıları Eldesiz Toplama (Örnek 1) ', desc='-', file='https://www.youtube.com/embed/LbFfUVByBAE'),
            LearningLectureYoutube(id=10049, name='İki Basamaklı Sayıları Eldesiz Toplama (Örnek 2) ', desc='-', file='https://www.youtube.com/embed/xTC_U5D1zS8'),
            LearningLectureYoutube(id=10050, name='İki Basamaklı Sayıları Basamaklarına Ayırarak Toplama İşlemi', desc='-', file='https://www.youtube.com/embed/uF1f3xiqcxA'),
            LearningLectureYoutube(id=10051, name='Bir Basamaklı Sayıları Eklemek İçin Eldeli Toplama İşlemi ', desc='-', file='https://www.youtube.com/embed/FwyVd1DPH3g'),
            LearningLectureYoutube(id=10052, name='10’lu Gruplara Ayırarak Toplama', desc='-', file='https://www.youtube.com/embed/_LU7GDEpc2E'),
            LearningLectureYoutube(id=10053, name='İki Basamaklı Sayıları Onluk Bozarak Çıkarma (Örnek 1) ', desc='-', file='https://www.youtube.com/embed/nRwTpa8Hw3w'),
            LearningLectureYoutube(id=10054, name='Ödünç alma olmadan iki basamaklı sayılarla çıkarma (2. örnek)', desc='-', file='https://www.youtube.com/embed/3HvljNdb_q4'),
            LearningLectureYoutube(id=10055, name='Bir Basamaklı Sayıları Onluk Bozarak Çıkarma', desc='-', file='https://www.youtube.com/embed/YxMYffkRYp0'),
            LearningLectureYoutube(id=10056, name='10’lu Gruplara Ayırarak Toplama: 53+17 ', desc='-', file='https://www.youtube.com/embed/52q80JW2Vsg'),
            LearningLectureYoutube(id=10058, name='İki Basamaklı Sayıları Toplamanın Değişik Yolları ', desc='-', file='https://www.youtube.com/embed/aa9FgSuYoGQ'),
            LearningLectureYoutube(id=10059, name='Toplama ve Çıkarma İşleminde Sayı Doğrusu Kullanma', desc='-', file='https://www.youtube.com/embed/HIZx1KAAQcc'),
            LearningLectureYoutube(id=10061, name='Eldeli Toplama İşleminin Açıklaması', desc='-', file='https://www.youtube.com/embed/3h3ofBKhR44'),
            LearningLectureYoutube(id=10063, name='Onluk Bozarak (Yan Basamaktan Ödünç Alarak) Çıkarma', desc='-', file='https://www.youtube.com/embed/82I8GNAbQEw'),
            LearningLectureYoutube(id=10064, name='Sayı Doğrusunda Toplama ve Çıkarma Problemleri ', desc='-', file='https://www.youtube.com/embed/DFKfWPcYdrg'),
            LearningLectureYoutube(id=10065, name='Çıkarma Alıştırması: Kaybolan Tenis Topları ', desc='-', file='https://www.youtube.com/embed/phX4zMCmzFs'),
            LearningLectureYoutube(id=10066, name='Toplama Alıştırması: Atlar ', desc='-', file='https://www.youtube.com/embed/qccqM_0-Rz4'),
            LearningLectureYoutube(id=10067, name='Çıkarma Alıştırması: Cuma Günü Kar Yağdı! ', desc='-', file='https://www.youtube.com/embed/gIvlAQI8BA4'),
            LearningLectureYoutube(id=10068, name='Çıkarma Alıştırması: Kuru Boyalar', desc='-', file='https://www.youtube.com/embed/LR5NeIBxJgs'),
            LearningLectureYoutube(id=10069, name='Çıkarma Alıştırması: Basketbol', desc='-', file='https://www.youtube.com/embed/wXgCtMQAc9E'),
            LearningLectureYoutube(id=10070, name='Toplama Alıştırması: Denizyıldızları Ülkesi ', desc='-', file='https://www.youtube.com/embed/21QRZGiUXCI'),
            LearningLectureYoutube(id=10071, name='Toplama Alıştırması: Zarın Üzerindeki Noktalar', desc='-', file='https://www.youtube.com/embed/n-0xVg0tQu8'),
            LearningLectureYoutube(id=10072, name='5’er 5’er Ritmik Sayma ', desc='-', file='https://www.youtube.com/embed/Qc2MgqmN0ss'),
            LearningLectureYoutube(id=10073, name='10’ar 10’ar Ritmik Sayma', desc='-', file='https://www.youtube.com/embed/oAMczrP3qlw'),
            LearningLectureYoutube(id=10074, name='100’er 100’er Ritmik Sayma', desc='-', file='https://www.youtube.com/embed/lGW11Skef2o'),
            LearningLectureYoutube(id=10075, name='100’den Küçük Sayılarla Toplama ve Çıkarmada Eksik Terimi Bulma', desc='-', file='https://www.youtube.com/embed/BZEEJugTk38'),

            LearningLectureYoutube(id=10076, name='10 ya da 100 ile Toplama İşlemi', desc='-', file='https://www.youtube.com/embed/l60q5uU4BiE'),
            LearningLectureYoutube(id=10077, name='Birler, Onlar, Yüzler Basamaklarında Toplama İşlemi', desc='-', file='https://www.youtube.com/embed/JFWi1PSYT_s'),
            LearningLectureYoutube(id=10078, name='Üç Basamaklı Sayıları Eldesiz Toplama', desc='-', file='https://www.youtube.com/embed/5WfPR3G0GuE'),
            LearningLectureYoutube(id=10079, name='1, 10 ya da 100 Sayılarını Çıkarma İşlemi ', desc='-', file='https://www.youtube.com/embed/rZiA6pvS-hU'),
            LearningLectureYoutube(id=10080, name='Birler, Onlar ve Yüzler Basamaklarında Çıkarma İşlemi ', desc='-', file='https://www.youtube.com/embed/97Y8-nVg_dw'),
            LearningLectureYoutube(id=10081, name='Üç Basamaklı Sayılarda Onluk Bozmadan Çıkarma', desc='-',  file='https://www.youtube.com/embed/AtpPxqLoChI'),
            LearningLectureYoutube(id=10082, name='Üç Basamaklı Sayıların Toplama İşlemlerini Parça Parça Çözme', desc='-', file='https://www.youtube.com/embed/T10eqpcw7Yw'),
            LearningLectureYoutube(id=10083, name='Üç Basamaklı Sayıları Zihinden Toplama', desc='-', file='https://www.youtube.com/embed/rcctMmrVRBo'),
            LearningLectureYoutube(id=10084, name='10’lu ve 100’lü Gruplarla Toplama İşlemi', desc='-', file='https://www.youtube.com/embed/i-deH8f8Gtc'),
            LearningLectureYoutube(id=10085, name='Toplama ve Çıkarma İşleminde Sayı Doğrusu Kullanma Örneği', desc='-', file='https://www.youtube.com/embed/PKQhZfDiDSc'),

            LearningLectureYoutube(id=10086, name='Uzunluğa Göre Sıralama', desc='-', file='https://www.youtube.com/embed/nk5oLYxf8Dg'),
            LearningLectureYoutube(id=10087, name='Uzunluk Ölçme Alıştırması: Örnek 2 ', desc='-', file='https://www.youtube.com/embed/28A4oT3Kya4'),
            LearningLectureYoutube(id=10088, name='Farklı Birimlerle Uzunluk Ölçme', desc='-', file='https://www.youtube.com/embed/RUvPNTBbuwM'),
            LearningLectureYoutube(id=10089, name='Uzunlukların Karşılaştırılması', desc='-', file='https://www.youtube.com/embed/j92Isgr_HJs'),
            LearningLectureYoutube(id=10090, name='Uzunlukları Tahmin Etme', desc='-', file='https://www.youtube.com/embed/uaD0-ylRswQ'),
            LearningLectureYoutube(id=10091, name='Uzunluk ile İlgili Alıştırmalar ', desc='-', file='https://www.youtube.com/embed/kH-3AuZyOik'),
            LearningLectureYoutube(id=10092, name='Uzunluk Ölçme Alıştırması: Altın Heykel', desc='-', file='https://www.youtube.com/embed/gVIprgdMvuc'),
            LearningLectureYoutube(id=10093, name='Şekil Grafikleri ', desc='-', file='https://www.youtube.com/embed/sHvBI7daXm0'),
            LearningLectureYoutube(id=10094, name='Şekil Grafikleri ve Çizgi Grafikleri Çizme', desc='-', file='https://www.youtube.com/embed/lux50HaafZw'),
            LearningLectureYoutube(id=10095, name='Sütun Grafiklerini Okuma: Kemikler', desc='-', file='https://www.youtube.com/embed/ND-RU8CJDFw'),
            LearningLectureYoutube(id=10096, name='Sütun Grafiklerini Okuma: Bisikletler', desc='-',  file='https://www.youtube.com/embed/hhz48zw0ooc'),
            LearningLectureYoutube(id=10097, name='Şekil ve Sütun Grafikleri Oluşturma 1', desc='-', file='https://www.youtube.com/embed/JZa6pyiP6QA'),
            LearningLectureYoutube(id=10098, name='Çizgi Grafikleri', desc='-', file='https://www.youtube.com/embed/9edGzDOwweM'),
            LearningLectureYoutube(id=10099, name='Şekil Grafikleri ve Çizgi Grafikleri Çizme', desc='-', file='https://www.youtube.com/embed/lux50HaafZw'),
            LearningLectureYoutube(id=10100, name='Çizgi Grafikleri Tekrar - (pdf)', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10101, name='Saat Okuma Alıştırması 1. Örnek', desc='-', file='https://www.youtube.com/embed/DhVAglJUxS4'),
            LearningLectureYoutube(id=10102, name='Saat Okuma Alıştırması 2. Örnek', desc='-', file='https://www.youtube.com/embed/JQwr4touKvI'),
            LearningLectureYoutube(id=10103, name='Paraları Sayma', desc='-', file='https://www.youtube.com/embed/CUbUDsX8cdM'),
            LearningLectureYoutube(id=10104, name='Bozuk Paraları Sayma', desc='-', file='https://www.youtube.com/embed/aBxnzsIURXc'),

            LearningLectureYoutube(id=10105, name='Şekil Problemi: Kuzen Cancin’in Şekil Koleksiyonu', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10106, name='Geometrik Şekilleri Tanıma', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10107, name='Geometrik Şekil Çizimi', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10108, name='Yarımlar ve Çeyrekler', desc='-', file='https://www.youtube.com/embed/'),
            LearningLectureYoutube(id=10109, name='Dairelerin ve Dikdörtgenlerin Eşit Parçaları', desc='-', file='https://www.youtube.com/embed/'),

            LearningLectureYoutube(id=10110, name='Basit Toplama İşlemleri', desc='-', file='https://www.youtube.com/embed/jpm1rBNwe6c'),
            LearningLectureYoutube(id=10111, name='Basit Çıkarma İşlemleri', desc='-', file='https://www.youtube.com/embed/H4UgtS4XWTY'),
            LearningLectureYoutube(id=10119, name='Onluk Bozarak (Yan Basamaktan Ödünç Alarak) Çıkarma', desc='-', file='https://www.youtube.com/embed/82I8GNAbQEw'),
            LearningLectureYoutube(id=10125, name='Üç Basamaklı Sayılarla Toplama İşlemi', desc='-', file='https://www.youtube.com/embed/Ra7Q9g8_iXw'),
            LearningLectureYoutube(id=10126, name='Üç Basamaklı Sayılarla Onluk Bozarak Çıkarma', desc='-', file='https://www.youtube.com/embed/vMraVAuVL0s'),
            LearningLectureYoutube(id=10127, name='Üç Basamaklı Sayılarla Çıkarma İşleminde İki Kere Onluk Bozma ( Yan Basamaktan Ödünç Alma )', desc='-', file='https://www.youtube.com/embed/9l1M4LnIX00'),
            LearningLectureYoutube(id=10128, name='Üç Basamaklı Sayılarla Çıkarma İşleminde 0’dan Ödünç Alma ', desc='-', file='https://www.youtube.com/embed/Ue5ceSyMdfc'),
            LearningLectureYoutube(id=10129, name='Onluk Bozmadan Zihinden Çıkarma Yapma Tekniği', desc='-', file='https://www.youtube.com/embed/S5wfIexs27U'),

        ])

    def handle(self, *args, **options):
        self._data_crate()
