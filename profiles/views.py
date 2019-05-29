from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404,HttpResponseRedirect,JsonResponse
from post.models import Post
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# def profile(request):
# 	if request.method=="POST":
# 		form=ProfileForm(request.POST or None,request.FILES)
# 		if form.is_valid():
# 			f=form.save(commit=False)
# 			f.user=request.user
# 			f.save()
# 			return redirect('post_app:index')
# 	else:
# 		form=ProfileForm()
# 	context={'form':form,}
# 	return render(request,'profiles/profileform.html',context)

@login_required()
def profile_update(request):
	if request.method=="POST":
		form=ProfileForm(request.POST or None,request.FILES,instance=request.user.profile)
		if form.is_valid():
			f=form.save(commit=False)
			f.user=request.user
			f.save()
			return redirect('post_app:index')
	else:
		form=ProfileForm(instance=request.user.profile)
	context={'form':form,}
	return render(request,'profiles/profile-update.html',context)	


def Userfollow(request,username,*args,**kwargs):
	is_follow=False
	user_f=get_object_or_404(User,username=username)
	user_add=request.user
	if user_f in user_add.profile.following.all():
		user_add.profile.following.remove(user_f)
		is_follow=False
	else:
		user_add.profile.following.add(user_f)
		is_follow=True
	return redirect(user_f.profile.get_absolute_url())		


@login_required()
def search(request):
			# qs=User.objects.all()
			qs=Post.objects.all()
			qs_u=User.objects.all()
			query=request.GET.get('q')
			if query:
				# qs=qs.filter(Q(username__icontains=query)					
				# 	)
				qs=qs.filter(Q(content__icontains=query)|
					Q(author__username__icontains=query)
					)
				qs_u=qs_u.filter(
					Q(username__icontains=query)
					)	
			return render(request,"profiles/search.html",{'posts':qs,'qs_u':qs_u})

login_required()
def profile(request,author,**kwargs):
	user=get_object_or_404(User,username=author)
	post=Post.objects.filter(author=user).order_by('-creat_at')
	post_c=Post.objects.filter(author=user).count()
	user_p=User.objects.get(username=user)
	if user_p in request.user.profile.following.all():
		is_follow=True
	else:
		is_follow=False
	active_p=True

	context={'post':post,'user_p':user_p,'is_follow':is_follow,'active_p':active_p,'post_c':post_c}
	return render(request,'profiles/profile.html',context)

login_required()
def profile_p(request,author,**kwargs):
	user=get_object_or_404(User,username=author)
	post=Post.objects.filter(author=user).order_by('-creat_at')
	active_pp=True
	user_p=User.objects.get(username=user)
	context={'post':post,'user_p':user_p,'active_pp':active_pp,}
	return render(request,'profiles/photo.html',context)

login_required()
def profile_a(request,author,**kwargs):
	user=get_object_or_404(User,username=author)
	post=Post.objects.filter(author=user).order_by('-creat_at')
	user_p=User.objects.get(username=user)
	active_a=True
	context={'post':post,'user_p':user_p,'active_a':active_a}
	return render(request,'profiles/about.html',context)

def follow_list(request):
	user=request.user
	context={
		'user':user
	}
	return render(request,'profiles/follow_info.html',context)


