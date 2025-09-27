from django.shortcuts import render , get_object_or_404
from apps.core.models import InternationalExchangeProgram , HonoraryProfessors , InternationalStudents , News , Hostel , HostelImages
from django.core.paginator import Paginator


# regions = [
#     {
#         "title": "Qoraqalpog‘iston",
#         "title_uz": "Qoraqalpog‘iston",
#         "title_en": "Karakalpakstan",
#         "title_ru": "Каракалпакстан",
#         "link": "https://uzbekistan.travel/uz/r/qoraqalpogiston/",
#         "img": "static/img/regions/bukhara.jpg",
#     },
#     {
#         "title": "Andijon viloyati",
#         "title_uz": "Andijon viloyati",
#         "title_en": "Andijan region",
#         "title_ru": "Андижанская область",
#         "link": "https://uzbekistan.travel/uz/r/andijon-viloyati/",
#         "img": "static/img/regions/andijan.jpg",
#     },
#     {
#         "title": "Xorazm viloyati",
#         "title_uz": "Xorazm viloyati",
#         "title_en": "Khorezm region",
#         "title_ru": "Хорезмская область",
#         "link": "https://uzbekistan.travel/uz/r/xorazm-viloyati/",
#         "img": "static/img/regions/khorezm.jpg",
#     },
#     {
#         "title": "Samarqand viloyati",
#         "title_uz": "Samarqand viloyati",
#         "title_en": "Samarkand region",
#         "title_ru": "Самаркандская область",
#         "link": "https://uzbekistan.travel/uz/r/samarqand-viloyati/",
#         "img": "static/img/regions/samarkand.jpg",
#     },
#     {
#         "title": "Qashqadaryo viloyati",
#         "title_uz": "Qashqadaryo viloyati",
#         "title_en": "Kashkadarya region",
#         "title_ru": "Кашкадарьинская область",
#         "link": "https://uzbekistan.travel/uz/r/qashqadaryo-viloyati/",
#         "img": "static/img/regions/kashkadarya.jpg",
#     },
#     {
#         "title": "Jizzax viloyati",
#         "title_uz": "Jizzax viloyati",
#         "title_en": "Jizzakh region",
#         "title_ru": "Джизакская область",
#         "link": "https://uzbekistan.travel/uz/r/jizzax-viloyati/",
#         "img": "static/img/regions/jizzakh.jpg",
#     },
#     {
#         "title": "Navoiy viloyati",
#         "title_uz": "Navoiy viloyati",
#         "title_en": "Navoi region",
#         "title_ru": "Навоийская область",
#         "link": "https://uzbekistan.travel/uz/r/navoiy-viloyati/",
#         "img": "static/img/regions/navaiy.jpg",
#     },
#     {
#         "title": "Surxondaryo viloyati",
#         "title_uz": "Surxondaryo viloyati",
#         "title_en": "Surkhandarya region",
#         "title_ru": "Сурхандарьинская область",
#         "link": "https://uzbekistan.travel/uz/r/surxondaryo-viloyati/",
#         "img": "static/img/regions/surkhandarya.png",
#     },
#     {
#         "title": "Namangan viloyati",
#         "title_uz": "Namangan viloyati",
#         "title_en": "Namangan region",
#         "title_ru": "Наманганская область",
#         "link": "https://uzbekistan.travel/uz/r/namangan-viloyati/",
#         "img": "static/img/regions/namangan.jpg",
#     },
#     {
#         "title": "Sirdaryo viloyati",
#         "title_uz": "Sirdaryo viloyati",
#         "title_en": "Syrdarya region",
#         "title_ru": "Сырдарьинская область",
#         "link": "https://uzbekistan.travel/uz/r/sirdaryo-viloyati/",
#         "img": "static/img/regions/syrdarya.jpg",
#     },
#     {
#         "title": "Farg‘ona viloyati",
#         "title_uz": "Farg‘ona viloyati",
#         "title_en": "Fergana region",
#         "title_ru": "Ферганская область",
#         "link": "https://uzbekistan.travel/uz/r/fargona-viloyati/",
#         "img": "static/img/regions/fergana.jpg",
#     },
# ]
# for region in regions:
#     AboutUzbekistan.objects.get_or_create(
#         title=region["title"],
#         defaults={
#             "title_uz": region["title_uz"],
#             "title_en": region["title_en"],
#             "title_ru": region["title_ru"],
#             "link": region["link"],
#             "img": region["img"],
#         }
#     )


# educational_areas = [
#     {
#         "cipher": "60310100",
#         "title_uz": "Iqtisodiyot (tarmoqlar va sohalar bo‘yicha)",
#         "title_en": "Economics (by industries and sectors)",
#         "title_ru": "Экономика (по отраслям и сферам)",
#         "e_type_uz": "Bakalavr",
#         "e_type_en": "Bachelor",
#         "e_type_ru": "Бакалавр",
#         "e_form_uz": "Kunduzgi",
#         "e_form_en": "Full-time",
#         "e_form_ru": "Очная",
#         "e_language_uz": "Ingliz tili",
#         "e_language_en": "English",
#         "e_language_ru": "Английский",
#     },
#     {
#         "cipher": "60410100",
#         "title_uz": "Buxgalteriya hisobi va audit (tarmoqlar bo‘yicha)",
#         "title_en": "Accounting and Auditing (by sectors)",
#         "title_ru": "Бухгалтерский учет и аудит (по отраслям)",
#         "e_type_uz": "Bakalavr",
#         "e_type_en": "Bachelor",
#         "e_type_ru": "Бакалавр",
#         "e_form_uz": "Kunduzgi",
#         "e_form_en": "Full-time",
#         "e_form_ru": "Очная",
#         "e_language_uz": "Ingliz tili",
#         "e_language_en": "English",
#         "e_language_ru": "Английский",
#     },
#     # shu yerga boshqa yo‘nalishlarni ham xuddi shu formatda qo‘shasiz
# ]


# # Bulk create
# objs = [
#     EducationalAreas(
#         cipher=item["cipher"],
#         title_uz=item["title_uz"],
#         title_en=item["title_en"],
#         title_ru=item["title_ru"],
#         e_type_uz=item["e_type_uz"],
#         e_type_en=item["e_type_en"],
#         e_type_ru=item["e_type_ru"],
#         e_form_uz=item["e_form_uz"],
#         e_form_en=item["e_form_en"],
#         e_form_ru=item["e_form_ru"],
#         e_language_uz=item["e_language_uz"],
#         e_language_en=item["e_language_en"],
#         e_language_ru=item["e_language_ru"],
#     )
#     for item in educational_areas
# ]

# EducationalAreas.objects.bulk_create(objs)
# print("EducationalAreas data successfully inserted ✅")




def home(request):
    news = News.objects.all()[:3].defer('description' , 'description_uz' , 'description_en' , 'description_ru')
    context = {
        'news': news
    }
    return render(request, 'index.html' , context)

def all_news(request):
    news = News.objects.all().defer('description' , 'description_uz' , 'description_en' , 'description_ru')
    paginator = Paginator(news, 10)
    page = request.GET.get('page')
    news = paginator.get_page(page)
    context = {
        'news': news
    }

    return render(request, 'all-news.html' , context)


def single_news(request , id):
    news = News.objects.get(id=id)
    others = News.objects.exclude(id=id).defer('description' , 'description_uz' , 'description_en' , 'description_ru')
    context = {
        'news': news,
        'others': others
    }
    return render(request, 'news-single.html' , context)

def honorary_professors(request):
    honorary_professors = HonoraryProfessors.objects.all()
    return render(request, 'international-honorary-professors.html', {'HP': honorary_professors})


def international_students(request):
    students = InternationalStudents.objects.prefetch_related('images').all()
    return render(request, 'international-students.html', {'students': students})


def hostel_for_foreign_students(request):
    hostel = Hostel.objects.all()
    paginator = Paginator(hostel, 5)
    page = request.GET.get('page')
    hostel = paginator.get_page(page)
    context = {
        'hostels': hostel
    }
    return render(request, 'admission/hostel-for-foreign-students.html', context)


def single_hostel(request , id):
    hostel = get_object_or_404(
        Hostel.objects.prefetch_related('images'),
        id=id
    )
    others = Hostel.objects.exclude(id=id)
    context = {
        'hostel': hostel,
        'others': others,
        'images': hostel.images.all()
    }
    return render(request, 'single-hostel.html' , context)
