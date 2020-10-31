from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.http import Http404
from .forms import Postemail, Postcomment
from django.core.mail import send_mail
# Create your views here.
def get_post(request):
    post = Post.objects.filter(status='published')
    return render(request, 'post/list_post.html', {'post': post})

def get_post_detail(request, year, month, day, slug_post):
    context = {}
    post = get_object_or_404(Post, status='published', publish__year=year, publish__month=month, publish__day=day, slug=slug_post)
    qset = post.comments.filter()
    print("qset is : ", qset)
    if request.method == 'POST':
        print("method is post")
        commentform = Postcomment(request.POST)
        if commentform.is_valid():
            print("form is valid")
            comdata = commentform.save(commit=False)
            comdata.com = post
            comdata.save()
            print(comdata.name)
            print(comdata.com)
            commentform = Postcomment()
            context['comdata'] = comdata
        else:
            print("form is not valid")
    else:
        print("method is get")
        commentform = Postcomment()
    context['post'] = post
    context['count'] = len(qset)
    context['qset'] = qset
    context['commentform'] = commentform
    return render(request, 'post/detail_post.html', context)
    # try:
    #     post = Post.objects.get(status='published', publish__year=year, publish__month=month, publish__day=day, slug=slug_post)
    # except Post.DoesNotExist:
    #     raise Http404("No Post matches the given query.")
    # #print(post)
    # return render(request, 'blog/detail_post.html', {'post': post})

def emailForm(request, slug_post):
    context={}
    post = get_object_or_404(Post, status='published', slug=slug_post)
    print("url is : ", request.build_absolute_uri(post.get_absolute_url()))
    if request.method == 'POST':
        print("method is post")
        email = Postemail(request.POST)
        if email.is_valid():
            print("form is valid")
            url = request.build_absolute_uri(post.get_absolute_url())
            uname = email.cleaned_data['name']
            subject = "{} recommends you to read '{}'".format(email.cleaned_data['name'], post.title)
            message = "Read '{}' at {} \n\n\n comments are {}".format(post.title, url, email.cleaned_data['comments'])
            send_mail(subject, message, 'abhisheksoni88114@gmail.com', [email.cleaned_data['to']])
            context['success'] = True
        else:
            print("form is not valid")
    else:
        print("method is get")
        email = Postemail()
    context['title'] = post.title
    context['email'] = email
    return render(request, 'post/emailform.html', context)