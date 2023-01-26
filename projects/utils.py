from django.db.models import Q 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project, Tag


def projectSearch(request):
    q = ''

    if request.GET.get('q'):
        q = request.GET.get('q')

    tag = Tag.objects.filter(name__icontains=q)
    projects = Project.objects.distinct().filter(Q(title__icontains=q) 
                                                | Q(description__icontains=q)
                                                | Q(owner__name__icontains=q)
                                                | Q(tags__in=tag))
    return projects, q


def paginateProjects(request, results, projects):
    page = 1
    paginator = Paginator(projects, results)

    try:
        page = request.GET.get('page')
        projects = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)


    leftIndex = int(page) - 4
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 5
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return projects, custom_range
