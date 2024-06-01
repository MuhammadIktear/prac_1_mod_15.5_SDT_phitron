from django.shortcuts import redirect, render
from .forms import musicianForm
from musician.models import Musician
from musician.forms import musicianForm
# Create your views here.
def add_musician(request):
    if request.method=='POST':
        add_form=musicianForm(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect('add_musician')
    else:
        add_form=musicianForm()
    return render(request,'add_musician.html',{'form':add_form,'text':'yes'})

def view_musician(request, id):
    post = Musician.objects.get(pk=id)
    post_form = musicianForm(instance=post)
    if request.method == 'POST':
        post_form = musicianForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    return render(request, 'add_musician.html', {'form': post_form, 'text': 'no', 'post': post})


def edit_musician(request, id):
    post = Musician.objects.get(pk=id)
    if request.method == 'POST':
        post_form = musicianForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    else:
        post_form = musicianForm(instance=post)
    return render(request, 'add_musician.html', {'form': post_form, 'text': 'no', 'post': post})


def delete_musician(request,id):
    post=Musician.objects.get(pk=id)
    post.delete()
    return redirect('homepage')