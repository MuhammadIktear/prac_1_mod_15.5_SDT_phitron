from django.shortcuts import redirect, render
from .forms import albumForm 
from. models import Album
def add_album(request):
    if request.method == 'POST':
        album_form = albumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = albumForm()

    return render(request, 'add_album.html', {'form': album_form,'text':'yes'})


def edit_album(request,id):
    post=Album.objects.get(pk=id)
    post_form=albumForm(instance=post)
    if request.method=='POST':
        post_form=albumForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')

    return render(request,'add_album.html',{'form':post_form,'text':'no'})
        
def del_album(request,id):
    post=Album.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
        

