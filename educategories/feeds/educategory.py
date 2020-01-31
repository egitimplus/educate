from educategories.models import  EduCategory


class EduCategoryRepository:

    def detail(self, pk):
        category = EduCategory.objects.values_list('id', 'name').filter(id=pk).first()

        return {
            'id': category[0],
            'name': category[1]
        }


    def breadcrumb(self, pk):

        category = EduCategory.objects.filter(id=pk).first()

        # breadcrumb oluşturalım
        category_list = [category.lesson_id, category.subject_id, category.unit_id, category.id]
        categories = EduCategory.objects.filter(id__in=category_list).order_by('depth').values('id', 'name',
                                                                                            'parent_id', 'depth')
        return categories




