import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .forms import CommentForm,FeedForm
from .models import Feed

def home(request):
    return  render (request, 'Bus project/API MAP.html')
def new(request):
    return render (request, 'new.html')
def create(request):
    if(request.method == "POST"):
        post = Feed()
        post.location = request.POST['location']
        post.save()
    return redirect ('home')
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    comment_form = CommentForm()
    return render(request, 'API MAP.html ', {'post_detail':post_detail, 'comment_form':comment_form})
def feedcreate(request):
    if request.method == 'POST' :
        pass
    else :
        form = FeedForm()
    return render(request, 'API MAP.html',{'form':form})
def Comment (request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form=CommentForm()
    return render(request, 'API MAP.html',{'post_detail':post_detail,'comment_form':comment_form})

def create_comment (requset, post_id):
    if requset.method == "POST":
        filled_form = CommentForm(request.POST)
        if filled_form.is_valid():
            finished_form = filled_form.save(commit = False)
            finished_form.post = get_object_or_404 (Feed, pk=post_id)
            finished_form.save()
            return redirect('detail', post_id)
    else :
        filled_form = CommentForm()
    return render ( requset, 'samchung/create_comment/<int:post_id>t',{'filled_form':filled_form} )

def comment_create_ajax(requset):
    comment = Comment()
    comment.body = request.POST.get('body')
    comment.feed = get_object_or_404(Blog, pk = request.POST.get('post_id'))
    comment.save()
    ret ={
        'body' :comment.body,
    }
    return HttpResponse(json.dumps(ret), content_type="application/json")