from django.db.models.signals import pre_delete
from django.dispatch import receiver
from questions.models import Question, QuestionAnswer, QuestionExam
from library.feeds import send_question_change_message_to_users as send_message


@receiver(pre_delete, sender=Question)
def delete_question_relations(sender, instance):
    """
    Soru silinmeden önce (pre_delete)
    --------------------------------------
    Aşağıdaki işlemler ilişkili olduğu için otomatik siliniyor fakat
    yine de silerek kontrolünü sağlayalım.
    """
    # eğer instance bulunamazsa silme işlemleri yapılmasın.
    # kayıt işleminin pre_save çağırıldığında instance henüz olmadığı için silme yapılmayacak
    if instance.id:

        # question_components talosundaki soru tipi ilişkileri silinir
        instance.component.clear()

        # source_question tabosundaki kaynak ilişkileri silinir
        instance.source_questions.clear()

        # question_exam tabosundaki kaynak ilişkileri silinir
        QuestionExam.objects.filter(question_id=instance.id).delete()

        # question_answer tablosundaki soru cevap şık ilişkileri silinir
        # bu silindiğinde yeni bir signal çağırılıp components_question_answer tablosunda silinme
        # işlemi gerçekleşecek
        QuestionAnswer.objects.filter(question_id=instance.id).delete()

        # sorunun silinmesi nedeniyle testteki sorularda silinecek.
        # soruyu teste ekleyen kullanıcılara bu bilgiyi gönderelim.
        send_message(instance, action='delete')

        # test_question tablosundaki test ilişkileri silinir
        instance.test_questions.clear()

        # question_unique tablosundaki benzersiz soru bilgileri güncellenir
        old_question_unique_count = Question.objects.filter(question_unique_id=instance.question_unique_id).count()

        if old_question_unique_count < 2:
            # QuestionUnique.objects.filter(id=instance.question_unique_id).delete()
            instance.question_unique.remove()






