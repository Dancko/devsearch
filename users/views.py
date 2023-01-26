from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, EditAccountForm, SkillForm, MessageForm
from .models import Profile, Skill, Message
from .utils import profileSearch, paginateProfiles


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'This user does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'User was logged in')
            return redirect(request.GET['next'] if 'next' in request.GET else 'account')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {'page': page}
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def logoutPage(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def registerPage(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User was successfully created')
            login(request, user)
            return redirect('edit_account')
        else:
            messages.error(request, "An error occurred during registeration")

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles, q = profileSearch(request)
    custom_range, profiles = paginateProfiles(request, 3, profiles)


    context = {'profiles': profiles, 'q': q, 'custom_range': custom_range}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user_profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile 
    skills = profile.skill_set.all()
    context = {'profile': profile, 'skills': skills}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    page = 'account'
    profile = request.user.profile
    form = EditAccountForm(instance=profile)
    if request.method == "POST":
        form = EditAccountForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form, 'page': page}
    return render(request, 'users/edit_account.html', context)


@login_required(login_url='login')
def addSkill(request):
    form = SkillForm()
    page = 'add'
    profile = request.user.profile

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, 'A new skill has been added')
            return redirect('account')

    context = {'form': form, 'page': page}
    return render(request, 'users/skill.html', context)


@login_required(login_url='login')
def editSkills(request, pk):
    page = 'edit'
    skill = Skill.objects.get(id=pk)

    form = SkillForm(instance=skill)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'The skill has been edited')
            return redirect('account')

    context = {'form': form, 'skill': skill, 'page': page}
    return render(request, 'users/skill.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    object = Skill.objects.get(id=pk)

    if request.method == "POST":
        object.delete()
        messages.error(request, "The skill was deleted")
        return redirect('account')

    context = {'object': object}
    return render(request, 'delete_template.html', context)


@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()

    context = {'messageRequests': messageRequests, 'unreadCount': unreadCount}
    return render(request, 'users/inbox.html', context)

@login_required(login_url='login')
def messageView(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message': message}
    return render(request, 'users/message.html', context)


def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None 

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.sender = sender 
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            messages.success(request, 'Your message has been successfully sent')
            return redirect('user_profile', pk=recipient.id)

    context = {'recipient': recipient, 'form': form}
    return render(request, 'users/message_form.html', context)
