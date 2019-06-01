from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.template.loader import render_to_string
from .forms import PostForm
from django.http import Http404,HttpResponseRedirect,JsonResponse
# from rest_framework.generics import ListAPIView
from django.views.decorators.csrf import csrf_exempt
from .models import Comments
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib import messages
# Create your views here.
# @csrf_exempt
@login_required()
def like(request,*args,**kwargs):
    # post=get_object_or_404(Post,id=request.POST.get("post_id"))
    post=get_object_or_404(Post,id=request.POST.get('id'))

    is_like=False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        is_like=False
    else:
        post.like.add(request.user)    
        is_like=True
    context={'post':post,'is_like':is_like,'total_likes':post.total_likes()}    
    if request.is_ajax():
        html=render_to_string('post_app/like_section.html',context,request=request)
        return JsonResponse({'form':html})
    

@login_required()
def index(request):
    i_following=request.user.profile.get_following()
    post=Post.objects.filter(author__in = i_following)
    post_u=Post.objects.filter(author = request.user).count() 

    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            s=form.save(commit=False)
            s.author=request.user
            s.save()
            messages.success(request,'Your Post Has Been Created.')
            return redirect('post_app:index')
    else:
        form=PostForm()
                          
    context={'post':post,'form':form,'post_u':post_u}
    return render(request,'post_app/index.html',context)


    

@login_required()
def details(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if post:
        post.increase()
    is_like=False
    if post.like.filter(id=request.user.id).exists():
        is_like=True
    comments=Comments.objects.filter(post=post,reply=None).order_by('-created_on')
    if request.method=="POST":
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_content=request.POST.get('comment_content')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comments.objects.get(id=reply_id)
            # post_d = get_object_or_404(Post,id=c_post)
            comment=Comments.objects.create(comment_content=comment_content,c_by=request.user,post=post,reply=comment_qs)
            comment.save()
            # return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form=CommentForm()
    context={'post':post,'comments':comments,'comment_form':comment_form,'is_like':is_like,'total_likes':post.total_likes()}
    if request.is_ajax():
        html=render_to_string('post_app/comment_section.html',context,request=request)
        return JsonResponse({'form':html})
    return render(request,'post_app/details.html',context)

@login_required()
def update(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if post.author==request.user:
        if request.method=="POST":
            form=PostForm(data=request.POST,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,'Your Post Updated Successfully.')
                return redirect('post_app:index')
        else:
            form=PostForm(instance=post)
    else:
        raise http404()
    context={'form':form}
    return render(request,'post_app/update.html',context)

@login_required()
def delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if post.author==request.user:
        post.delete()
        messages.success(request,'Your Post Deleted Successfully.')
    else:
        raise http404()
    return redirect('post_app:index')

@login_required()
def all_post(request):
    post=Post.objects.all().order_by('-creat_at')
    if request.method=="POST":
        form=PostForm(request.POST or None,request.FILES)
        if form.is_valid():
            s=form.save(commit=False)
            s.author=request.user
            s.save()
            return redirect('post_app:allposts')
    else:
        form=PostForm()
    return render(request,'post_app/all.html',{'post':post,'form':form})


def main(request):
    main=True
    return render(request,'post_app/main.html',{'main':main})    