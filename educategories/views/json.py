"""

getLessons +++++
getSubs +++
getQuestions +

-------------------------------------------------------------
GET - getLessons
-------------------------------------------------------------
[
    {
        "id": 1,
        "name": "Matematik",
        "active": 1
    }
]

-------------------------------------------------------------
GET - getCategory  - Kullanılmıyor
-------------------------------------------------------------
{
    "edu_categories": {
        "1": {
            "id": 1,
            "parent_id": null,
            "name": "Matematik",
            "children": [
                {
                    "id": 2,
                    "parent_id": 1,
                    "name": "Sayılar",
                    "children": [
                        {
                            "id": 6,
                            "parent_id": 2,
                            "name": "Tam Sayılar",
                            "children": [
                                {
                                    "id": 8,
                                    "parent_id": 6,
                                    "name": "Tek ve Çift Sayılar",
                                    "children": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    }
}

-------------------------------------------------------------
POST - addCategory             | create  | id
-------------------------------------------------------------

* eğer parent_id 0 değilse alt eleman oluşturması yapılır.
* post aynı endpointe yapılıyor

name - required
active
id - required (alt eleman için)

-------------------------------------------------------------
PUT - updateCategory             | update  | id
-------------------------------------------------------------
id - required

-------------------------------------------------------------
DEL - deleteCategory             | destroy  | id
-------------------------------------------------------------
id - required


-------------------------------------------------------------
GET - getSubs             | id
-------------------------------------------------------------
[
    {
        "id": 2,
        "parent_id": 1,
        "depth": 1,
        "name": "Sayılar",
        "slug": "sayilar",
        "active": 1,
        "created_at": null,
        "updated_at": null
    }
]

component/question/add-modal.js

-------------------------------------------------------------
GET - getQuestions               | id
-------------------------------------------------------------
[
    {
        "id": 1,
        "name": "",
        "active": 1,
        "source": "Source Adı Vardı Multiple Oldu",
        "part": "bölüm adı vardı multiple oldu"
    }
]

page/category/manage.js
component/question-type/add-sub.js

-------------------------------------------------------------
GET - getQuestionTypes             | id
-------------------------------------------------------------
[
    {
        "id": 1,
        "active": 1,
        "name": "Çıkarma işlemi",
        "level": 1,
        "seconds": 15,
        "edu_category_id": 4,
        "sub_question_types": [],
        "parent_question_types": [
            6,
            16
        ],
        "all_sub_question_types": [],
        "all_question_types": [
            6,
            16
        ]
    }
]



page/category/lesson.js
-------------------------------------------------------------
GET - getParents             |  id
-------------------------------------------------------------
[
    {
        "id": 1,
        "parent_id": null,
        "name": "Matematik"
    },
    {
        "id": 2,
        "parent_id": 1,
        "name": "Sayılar"
    },
    {
        "id": 3,
        "parent_id": 2,
        "name": "Temel Kavramlar"
    },
    {
        "id": 5,
        "parent_id": 3,
        "name": "Diğer Kavramlar"
    }
]

-------------------------------------------------------------
GET - getUserSubs             | id
-------------------------------------------------------------
[
    {
        "id": 3,
        "parent_id": 2,
        "name": "Temel Kavramlar",
        "active": 1,
        "percentage": 93
    }
]


-------------------------------------------------------------
GET - getUserLessons
-------------------------------------------------------------
[
    {
        "id": 1,
        "name": "Matematik",
        "active": 1,
        "percentage": 51
    }
]


-------------------------------------------------------------
GET - getUserQuestionTypes
-------------------------------------------------------------
[
    {
        "id": 24,
        "active": 1,
        "name": "Rakam tanımı",
        "percentage": 22
    }
]
"""
