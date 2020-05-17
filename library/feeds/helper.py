from educategories.feeds import EduCategoryRepository
from collections import Iterable                            # < py38


def flatten(items):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x


def search_id(match, data):
    """
    list içerisindeki elemanlarda id araması için
    eğer varsa elemanı döndürür
    """
    return [element for element in data if element['id'] == match]


def get_breadcrumb(pk):
    """
    verilen kategori id sinden breadcrumb dictionary döndürür.
    """
    edu_repo = EduCategoryRepository()

    return edu_repo.breadcrumb(pk)


def get_category(pk):
    """
    verilen kategori id sinden kategori bilgilerini döndürür.
    """
    edu_repo = EduCategoryRepository()

    return edu_repo.detail(pk)


def send_question_change_message_to_users(question, **kwargs):
    # TODO tests listesindeki test sahiplerine bilgilendirme gönderilecek. Bunun için message yapılmalı

    action = kwargs.pop('type', None)

    tests = []
    test_queryset = question.test_questions.all()
    for test in test_queryset:
        tests.append(test.id)

    # TODO kontrol bittiğinde silmeyi unutma


    if action == 'update':
        # 15 - kümeler testinde 14. numaralı soru kaynak sahibince güncellenmiştir.
        # Testi görüntülemek için tıklayın.
        print('güncelleme işlemi')
    elif action == 'delete':
        # 15 - kümeler testinde 14. numaralı soru kaynak sahibince silinmiş olup, soru testten çıkartılmıştır.
        # Testi görüntülemek için tıklayın.
        print('silme işlemi')
    elif action == 'disable':
        print('pasifleştirme işlemi')

