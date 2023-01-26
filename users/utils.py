from .models import Profile, Skill
from django.db.models import Q 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def profileSearch(request):
    q = ''
    if request.GET.get('q'):
        q = request.GET.get('q')

    skills = Skill.objects.filter(name__icontains=q)

    profiles = Profile.objects.distinct().filter(Q(name__icontains=q) | Q(short_intro__icontains=q) | Q(skill__in=skills))
    return (profiles, q) 


def paginateProfiles(request, results, profiles):
    paginator = Paginator(profiles, results)

    try:
        page = request.GET.get('page')
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    leftIndex = int(page) - 3
    if leftIndex < 1:
        leftIndex = 1
    rightIndex = int(page) + 3
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, profiles
