from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.utils import timezone 
from iniad.models import Comment
#from models import Article, Comment
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def top(request):
    return render(request, 'keijiban/top.html')


def subjects(request):
    return render(request, "keijiban/subjects.html")

def club(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_club'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()

    context = {
        'comments': Comment.objects.filter(channel='club')
    }
    return render(request, "keijiban/club.html", context)

def chat(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_chat'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()

    context = {
        'comments': Comment.objects.filter(channel='chat')
    }
    return render(request, "keijiban/chat.html", context)

def others(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_others'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()

    context = {
        'comments': Comment.objects.filter(channel='others')
    }
    return render(request, "keijiban/others.html", context)

def cs_exercise(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_cs_exercise'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()

    context = {
        'comments': Comment.objects.filter(channel='cs')
    }
    return render(request, "keijiban/cs_exercise.html", context)

def ls_exercise(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_ls_exercise'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()

    context = {
        'comments': Comment.objects.filter(channel='ls')
    }
    return render(request, "keijiban/ls_exercise.html", context)

def rw_exercise(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_rw_exercise'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()

    context = {
        'comments': Comment.objects.filter(channel='rw')
    }
    return render(request, "keijiban/rw_exercise.html", context)

def basic(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_basic'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()

    context = {
        'comments': Comment.objects.filter(channel='basic')
    }
    return render(request, "keijiban/basic.html", context)

def social(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_social'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()

    context = {
        'comments': Comment.objects.filter(channel='social')
    }
    return render(request, "keijiban/social.html", context)

def practice(request):
    if request.method == 'POST':
        comment=Comment(text=request.POST['text_practice'],
        posted_at=timezone.now(),
        channel=request.POST['channel'])
        comment.save()


    context = {
        'comments': Comment.objects.filter(channel='practice')
    }
    return render(request, "keijiban/practice.html", context)



#このしたデリート機能
def delete_cs(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(cs_exercise)

def delete_ls(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(ls_exercise)

def delete_rw(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(rw_exercise)

def delete_so(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(social)

def delete_ba(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(basic)

def delete_pr(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(practice)

def delete_ch(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(chat)

def delete_ot(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(others)

def delete_cl(request, comment_id):
    try:
        article = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Article does not exist")
    article.delete()
    return redirect(club)
