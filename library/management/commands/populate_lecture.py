from django.core.management.base import BaseCommand
from companies.models import *
from curricula.models import *
from publishers.models import *
from educategories.models import *
from questions.models import *
from components.models import *
from tests.models import *
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()


class Command(BaseCommand):

    def _data_crate(self):
        """
            Youtube olmayanlar
            #10027
            #10028
            #10035
            #10044
            #11100
        """

        content_type = ContentType.objects.get_for_model(LearningLectureYoutube)
        content_type_id = content_type.id

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10001, name='Küçük Sayılarla Sayma', subject_id=10001, object_id=10001, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10002, name='Sıralı Sayma', subject_id=10001, object_id=10002, position=2, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10003, name='Sayı Tablosu Oluşturma', subject_id=10002, object_id=10003, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10004, name='0 ile 120 Arasındaki Eksik Sayıları Bulma', subject_id=10002, object_id=10004, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10005, name='Şekillerle Sayma', subject_id=10003, object_id=10005,position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10006, name='Nesneleri Sayma Alıştırması: Balinaları, Koçları ve Çiçekleri Sayalım!', subject_id=10003, object_id=10006, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10007, name='Nesneleri Sayma Alıştırması: Köpekleri, Fareleri ve Kurabiyeleri Sayalım!', subject_id=10003, object_id=10007, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10008, name='10’a Kadar Olan Nesne Sayılarını Karşılaştırma',subject_id=10004, object_id=10008, position=1, content_type_id=content_type_id, summary='-',content='-', publisher_id=101),
            LearningLecture(id=10009, name='10’a Kadar Olan Sayıları Sayı Doğrusu Üzerinde Karşılaştırma',subject_id=10004, object_id=10009, position=1, content_type_id=content_type_id, summary='-',content='-', publisher_id=101),
            LearningLecture(id=10010, name='Kategorilere Göre Sayma',subject_id=10004, object_id=10010, position=1, content_type_id=content_type_id, summary='-',content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10011, name='Toplama', subject_id=10005, object_id=10011, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10012, name='Çıkarma', subject_id=10005, object_id=10012, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10013, name='5 Elde Etme', subject_id=10006, object_id=10013, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10014, name='Kutuları Doldurarak 10 Elde Etme', subject_id=10007, object_id=10014, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10015, name='10 ile Toplama İşlemi', subject_id=10007, object_id=10015, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10016, name='Toplama ve Çıkarma Alıştırması: Meyveleri Sayalım!', subject_id=10008, object_id=10016, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10017, name='10’a Kadar Olan Sayılarla Toplama ve Çıkarma İşlemi', subject_id=10008, object_id=10017, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10018, name='Toplama ve Çıkarma Arasındaki İlişki', subject_id=10009, object_id=10018, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10019, name='10’a Kadar Olan Sayılarla Toplama Problemleri', subject_id=10010, object_id=10019, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10020, name='10’a Kadar Olan Sayılarla Çıkarma Problemleri', subject_id=10010, object_id=10020, position=1,content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10021, name='10’lu Sayıların Toplam Halinde Gösterilmesi', subject_id=10011, object_id=10021, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10022, name='10’lu Sayılarla Alıştırma: Partiye Kaç Maymun Gelmeli?', subject_id=10011, object_id=10022, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10023, name='Basamak Değeri', subject_id=10012, object_id=10023, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10024, name='25 ile Basamak Değeri Alıştırması', subject_id=10012, object_id=10024, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10025, name='42 ile Basamak Değeri Alıştırması', subject_id=10012, object_id=10025, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10026, name='Büyüktür ve Küçüktür Simgeleri', subject_id=10013, object_id=10026, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10027, name='Karşılaştırma işaretlerinin bir daha gözden geçirilmesi - (pdf)', subject_id=10013, object_id=10027, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10028, name='Bu derste video veya makale yok. - (no content)', subject_id=10014, object_id=10028, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10029, name='Doğal Sayıları Karşılaştırma', subject_id=10015, object_id=10029, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10030, name='Toplama Alıştırması: 7 + 6', subject_id=10016, object_id=10011, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10031, name='Toplama Alıştırması: 8 + 7', subject_id=10016, object_id=10031, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10032, name='Toplama Alıştırması: 5 + 3 + 6', subject_id=10016, object_id=10032, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10033, name='Çıkarma Alıştırması: 14 - 6', subject_id=10017, object_id=10033, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10034, name='Eşittir İşareti', subject_id=10018, object_id=10034, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10035, name='Bu derste video veya makale yok.', subject_id=10019, object_id=10035, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10036, name='Toplama ve Çıkarma Alıştırması: Göl Canavarları ve Süper Kahramanlar', subject_id=10020, object_id=10036, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10037, name='Toplama ve Çıkarma Alıştırması: Spor Salonundaki Goriller', subject_id=10020, object_id=10037, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10038, name='Karşılaştırma Problemleri', subject_id=10021, object_id=10038, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10039, name='Karşılaştırma Problemleri', subject_id=10021, object_id=10039, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10040, name='Toplama İşlemine Örnekler', subject_id=10022, object_id=10040, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10041, name='Bir Sayıya 1 ve 10 Eklemek Arasındaki Fark', subject_id=10023, object_id=10041, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10042, name='Onlukları Eklerken Basamak Değerini Anlama', subject_id=10023, object_id=10042, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10043, name='Birlikleri Eklerken Basamak Değerini Anlama', subject_id=10023, object_id=10043, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10044, name='1’leri ve 10’ları toplamaya ilişkin yönlendirmeli alıştırmalar - (pdf)', subject_id=10023, object_id=10044, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10045, name='1 Çıkarmak ve 10 Çıkarmak Arasındaki Fark', subject_id=10024, object_id=10045, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10046, name='Birlikleri Çıkarırken Basamak Değerini Anlama', subject_id=10024, object_id=10046, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10047, name='Onlukları Çıkarırken Basamak Değerini Anlama', subject_id=10024, object_id=10047, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10048, name='İki Basamaklı Sayıları Eldesiz Toplama (Örnek 1)', subject_id=10025, object_id=10048, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10049, name='İki Basamaklı Sayıları Eldesiz Toplama (Örnek 2)', subject_id=10025, object_id=10049, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10050, name='İki Basamaklı Sayıları Basamaklarına Ayırarak Toplama İşlemi', subject_id=10025, object_id=10050, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10051, name='Bir Basamaklı Sayıları Eklemek İçin Eldeli Toplama İşlemi', subject_id=10025, object_id=10051, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10052, name='10’lu Gruplara Ayırarak Toplama', subject_id=10025, object_id=10052, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10053, name='İki Basamaklı Sayıları Onluk Bozarak Çıkarma (Örnek 1)', subject_id=10025, object_id=10053, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10054, name='Ödünç alma olmadan iki basamaklı sayılarla çıkarma (2. örnek)', subject_id=10026, object_id=10054, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10055, name='Bir Basamaklı Sayıları Onluk Bozarak Çıkarma', subject_id=10026, object_id=10055, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10056, name='10’lu Gruplara Ayırarak Toplama: 53+17', subject_id=10027, object_id=10056, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10057, name='10’lu Gruplara Ayırarak Toplama', subject_id=10027, object_id=10052, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10058, name='İki Basamaklı Sayıları Toplamanın Değişik Yolları', subject_id=10027, object_id=10058, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10059, name='Toplama ve Çıkarma İşleminde Sayı Doğrusu Kullanma', subject_id=10027, object_id=10059, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10060, name='İki Basamaklı Sayıları Eldesiz Toplama (Örnek 2)', subject_id=10028, object_id=10049, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10061, name='Eldeli Toplama İşleminin Açıklaması', subject_id=10028, object_id=10061, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10062, name='İki Basamaklı Sayıları Onluk Bozarak Çıkarma (Örnek 1)', subject_id=10029, object_id=10053, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10063, name='Onluk Bozarak (Yan Basamaktan Ödünç Alarak) Çıkarma', subject_id=10029, object_id=10063, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10064, name='Sayı Doğrusunda Toplama ve Çıkarma Problemleri', subject_id=10030, object_id=10064, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10065, name='Çıkarma Alıştırması: Kaybolan Tenis Topları', subject_id=10030, object_id=10065, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10066, name='Toplama Alıştırması: Atlar', subject_id=10030, object_id=10066, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10067, name='Çıkarma Alıştırması: Cuma Günü Kar Yağdı!', subject_id=10030, object_id=10067, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10068, name='Çıkarma Alıştırması: Kuru Boyalar', subject_id=10030, object_id=10068, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10069, name='Çıkarma Alıştırması: Basketbol', subject_id=10031, object_id=10069, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10070, name='Toplama Alıştırması: Denizyıldızları Ülkesi', subject_id=10031, object_id=10070, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10071, name='Toplama Alıştırması: Zarın Üzerindeki Noktalar', subject_id=10031, object_id=10071, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10072, name='5’er 5’er Ritmik Sayma', subject_id=10032, object_id=10072, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10073, name='10’ar 10’ar Ritmik Sayma', subject_id=10032, object_id=10073, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10074, name='100’er 100’er Ritmik Sayma', subject_id=10032, object_id=10074, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10075, name='100’den Küçük Sayılarla Toplama ve Çıkarmada Eksik Terimi Bulma', subject_id=10033, object_id=10075, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10076, name='10 ya da 100 ile Toplama İşlemi', subject_id=10034, object_id=10076, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10077, name='Birler, Onlar, Yüzler Basamaklarında Toplama İşlemi', subject_id=10034, object_id=10077, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10078, name='Üç Basamaklı Sayıları Eldesiz Toplama', subject_id=10034, object_id=10078, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10079, name='1, 10 ya da 100 Sayılarını Çıkarma İşlemi ', subject_id=10035, object_id=10079, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10080, name='Birler, Onlar ve Yüzler Basamaklarında Çıkarma İşlemi ', subject_id=10035, object_id=10080, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10081, name='Üç Basamaklı Sayılarda Onluk Bozmadan Çıkarma', subject_id=10035, object_id=10081, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10082, name='Üç Basamaklı Sayıların Toplama İşlemlerini Parça Parça Çözme', subject_id=10036, object_id=10082, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10083, name='Üç Basamaklı Sayıları Zihinden Toplama', subject_id=10036, object_id=10083, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10084, name='10’lu ve 100’lü Gruplarla Toplama İşlemi', subject_id=10036, object_id=10084, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10085, name='Toplama ve Çıkarma İşleminde Sayı Doğrusu Kullanma Örneği', subject_id=10036, object_id=10085, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10086, name='Uzunluğa Göre Sıralama', subject_id=10037, object_id=10086, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10087, name='Uzunluk Ölçme Alıştırması: Örnek 2 ', subject_id=10038, object_id=10087, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10088, name='Farklı Birimlerle Uzunluk Ölçme', subject_id=10038, object_id=10088, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10089, name='Uzunlukların Karşılaştırılması ', subject_id=10039, object_id=10089, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10090, name='Uzunlukları Tahmin Etme', subject_id=10039, object_id=10090, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10091, name='Uzunluk ile İlgili Alıştırmalar ', subject_id=10040, object_id=10091, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10092, name='Uzunluk Ölçme Alıştırması: Altın Heykel', subject_id=10040, object_id=10092, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10093, name='Şekil Grafikleri ', subject_id=10041, object_id=10093, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10094, name='Şekil Grafikleri ve Çizgi Grafikleri Çizme', subject_id=10041, object_id=10094, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10095, name='Sütun Grafiklerini Okuma: Kemikler', subject_id=10042, object_id=10095, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10096, name='Sütun Grafiklerini Okuma: Bisikletler ', subject_id=10042, object_id=10096, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10097, name='Şekil ve Sütun Grafikleri Oluşturma 1', subject_id=10042, object_id=10097, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10098, name='Çizgi Grafikleri', subject_id=10043, object_id=10098, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10099, name='Şekil Grafikleri ve Çizgi Grafikleri Çizme', subject_id=10043, object_id=10099, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10100, name='Çizgi Grafikleri Tekrar - (pdf)', subject_id=10043, object_id=10100, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10101, name='Saat Okuma Alıştırması 1. Örnek', subject_id=10044, object_id=10101, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10102, name='Saat Okuma Alıştırması 2. Örnek', subject_id=10044, object_id=10102, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10103, name='Paraları Sayma', subject_id=10045, object_id=10103, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10104, name='Bozuk Paraları Sayma', subject_id=10045, object_id=10104, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10105, name='Şekil Problemi: Kuzen Cancin’in Şekil Koleksiyonu', subject_id=10046, object_id=10105, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10106, name='Geometrik Şekilleri Tanıma', subject_id=10046, object_id=10106, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10107, name='Geometrik Şekil Çizimi', subject_id=10048, object_id=10107, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10108, name='Yarımlar ve Çeyrekler', subject_id=10049, object_id=10108, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10109, name='Dairelerin ve Dikdörtgenlerin Eşit Parçaları', subject_id=10049, object_id=10109, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
        ])

        LearningLecture.objects.bulk_create([
            LearningLecture(id=10110, name='Basit Toplama İşlemleri', subject_id=10050, object_id=10110, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10111, name='Basit Çıkarma İşlemleri', subject_id=10050, object_id=10111, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10112, name='Toplama Alıştırması: 8 + 7', subject_id=10051, object_id=10031, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10113, name='Çıkarma Alıştırması: 14 - 6', subject_id=10051, object_id=10033, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10114, name='10’lu Gruplara Ayırarak Toplama: 53+17 ', subject_id=10052, object_id=10056, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10115, name='10’lu Gruplara Ayırarak Toplama ', subject_id=10052, object_id=10052, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10116, name='İki Basamaklı Sayıları Toplamanın Değişik Yolları ', subject_id=10052, object_id=10058, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10117, name='Toplama ve Çıkarma İşleminde Sayı Doğrusu Kullanma', subject_id=10052, object_id=10059, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10118, name='İki Basamaklı Sayıları Eldesiz Toplama (Örnek 2)', subject_id=10053, object_id=10049, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10119, name='Onluk Bozarak (Yan Basamaktan Ödünç Alarak) Çıkarma', subject_id=10054, object_id=10119, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10120, name='Çıkarma Alıştırması: Kaybolan Tenis Topları ', subject_id=10055, object_id=10065, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10121, name='Toplama Alıştırması: Atlar ', subject_id=10055, object_id=10066, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10122, name='Çıkarma Alıştırması: Cuma Günü Kar Yağdı!', subject_id=10055, object_id=10067, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10123, name='Çıkarma Alıştırması: Kuru Boyalar', subject_id=10055, object_id=10068, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10124, name='Eldeli Toplama İşleminin Açıklaması ', subject_id=10056, object_id=10061, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10125, name='Üç Basamaklı Sayılarla Toplama İşlemi', subject_id=10056, object_id=10125, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10126, name='Üç Basamaklı Sayılarla Onluk Bozarak Çıkarma', subject_id=10057, object_id=10126, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10127, name='Üç Basamaklı Sayılarla Çıkarma İşleminde İki Kere Onluk Bozma ( Yan Basamaktan Ödünç Alma )', subject_id=10057, object_id=10127, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10128, name='Üç Basamaklı Sayılarla Çıkarma İşleminde 0’dan Ödünç Alma ', subject_id=10057, object_id=10128, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),
            LearningLecture(id=10129, name='Onluk Bozmadan Zihinden Çıkarma Yapma Tekniği', subject_id=10057, object_id=10129, position=1, content_type_id=content_type_id, summary='-', content='-', publisher_id=101),

        ])

    def handle(self, *args, **options):
        self._data_crate()


