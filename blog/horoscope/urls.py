from django.urls import path
from . import views

urlpatterns = [   
    # https://docs.djangoproject.com/en/4.2/topics/http/urls/#path-converters 
    # Path converters - <int:sign_zodiac> должна быть выше, так как str преобразует число к строке, что вызовет другую ф-ю. Порядок важен
    path('', views.index),
    path('type', views.type_info),
    path('type/<str:type_element>', views.element_info, name='type-elem-name'),
    path('<int:sign_zodiac>', views.get_info_sign_zodiac_by_number),
    path('<str:sign_zodiac>', views.get_info_sign_zodiac, name='horoscope-name'),
    # path("leo", views.leo),
    # path("scorpio", views.scorpio),
]