from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

zodiac_dict = {
    "aries": "Овен - 1-й знак",
    "taurus": "Телец - 2-й знак",
    "gemini": "Близнецы - 3-й знак",
    "cancer": "Рак - 4-й знак",
    "leo": "Лев - 5-й знак",
    "virgo": "Дева - 6-й знак",
    "libra": "Весы - 7-й знак",
    "scorpio": "Скорпион - 8-й знак",
    "segittarius": "Стрелец - 9-й знак",
    "capricorn": "Козерог - 10-й знак",
    "aquarius": "Водолей - 11-й знак",
    "pisces": "Рыбы - 12-й знак",
}

types_dict = {
    'fire' : ['aries', 'leo', 'segittarius'],
    'earth' : ['taurus', 'virgo', 'capricorn'],
    'air' : ['gemini', 'libra', 'aquarius'],
    'water' : ['cancer', 'scorpio', 'pisces']
}

# print(zodiac_dict.keys())

# def leo(request):
#     return HttpResponse('Znak Zodiac LEO')

# def scorpio(request):
#     return HttpResponse('Znak Zodiac SCORPIO')


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ""
    for sign in zodiacs:
        redirect_path = reverse("horoscope-name", args=[sign])
        li_elements += f'<li><a href="{redirect_path}">{sign.title()}</a></li>'
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)

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


def element_info(request, type_element):
    elements = types_dict.get(type_element)
    li_elements = ""
    for element in elements:
        redirect_path = reverse("type-elem-name", args=[element])
        li_elements += f'<li><a href="{redirect_path}">{element.title()}</a></li>'
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)


def get_info_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    if description:
        return HttpResponse(f"<h2>{description}</h2>")
    else:
        return HttpResponseNotFound(f"Unknown znak zodiac - {sign_zodiac}")




def get_info_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Неправильный порядковый номер - {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
