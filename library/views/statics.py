from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def company_types(request):
    return Response([
        {'id':1, 'name':'Okul'},
        {'id':2, 'name':'Dershane'}
    ])


@api_view()
def departments(request):
    return Response([
        {'id':1, 'name':'Fen Bilimleri  '},
        {'id':2, 'name': 'Eşit Ağırlık'},
        {'id':3, 'name': 'Sosyal Bilimler'}
    ])


@api_view()
def school_roles(request):
    return Response([
        {'id':1, 'name': 'Yönetici'},
        {'id':2, 'name': 'Öğretmen'},
        {'id':3, 'name': 'Öğrenci'}
    ])