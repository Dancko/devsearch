from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project, Tag
from .forms import CreateProjectForm, ReviewForm
from .utils import projectSearch, paginateProjects

# Create your views here.

def projects_list(request):
    projects, q = projectSearch(request)
    projects, custom_range = paginateProjects(request, 6, projects)
    
    print(projects)
    context = {'projects': projects, 'q': q,  
                'custom_range': custom_range}
    return render(request, 'projects_list.html', context)


def project_detail(request, pk):
    project = Project.objects.get(id=pk)

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.owner = request.user.profile
            review.save()
            project.getVotesCount
            messages.success(request, 'Your review has been submitted')
            return redirect('project_detail', pk=project.id)
    

    return render(request, 'project.html', {'project': project, 'form': form})


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = CreateProjectForm()

    if request.method == "POST":
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        form = CreateProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects_list')

    context = {'form': form}
    return render(request, 'create_project.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = CreateProjectForm(instance=project)

    if request.method == "POST":
        newtags = request.POST.get('newtags').replace(',', ' ').split()
        form = CreateProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('account')
    
    context = {'form': form, 'project': project}
    return render(request, 'create_project.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    object = Project.objects.get(id=pk)

    if request.method == "POST":
        object.delete()
        return redirect('account')

    context = {'object': object}
    return render(request, 'delete_template.html', context)



