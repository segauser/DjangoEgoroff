from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

zodiac_dict = {
    "aries": "Овен /Aries - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    "taurus": "Телец /Taurus - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    "gemini": "Близнецы /Gemini - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    "cancer": "Рак /Cancer - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    "leo": "Лев /Leo - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    "virgo": "Дева /Virgo - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    "libra": "Весы /Libra - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    "scorpio": "Скорпион /Scorpio - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    "segittarius": "Стрелец /Sagittarius - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    "capricorn": "Козерог /Capricorn - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    "aquarius": "Водолей /Aquarius - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    "pisces": "Рыбы /Pisces - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
}

types_dict = {
    'fire': ['aries', 'leo', 'segittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

# print(zodiac_dict.keys())

# def leo(request):
#     return HttpResponse('Znak Zodiac LEO')

# def scorpio(request):
#     return HttpResponse('Znak Zodiac SCORPIO')


def index(request):
    zodiacs = list(zodiac_dict)
    # li_elements += f'<li><a href="{redirect_path}">{sign.title()}</a></li>'
    context = {
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/index.html', context=context)

# TODO - сделать представление для horoscope/type
def type_info(request):
    types = list(types_dict)
    li_elements = ""
    for type in types:
        redirect_path = reverse("type-elem-name", args=[type])
        li_elements += f'<li><a href="{redirect_path}">{type.title()}</a></li>'
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)

# [x]TODO - сделать представление для horoscope/type/element
def element_info(request, type_element):
    elements = types_dict.get(type_element)
    li_elements = ""
    for element in elements:
        redirect_path = reverse("horoscope-name", args=[element])
        li_elements += f'<li><a href="{redirect_path}">{element.title()}</a></li>'
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_info_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict

    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
