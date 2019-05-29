from django.shortcuts import render,redirect
from .forms import RegistrationForm,ChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def signup(request):
	if request.method=="POST":
		form=RegistrationForm(request.POST or None)
		if form.is_valid():
			form.save()
			user=form.save()
			login(request,user,backend='django.contrib.auth.backends.ModelBackend')
			messages.success(request,'Your Account Has Created successfuly.')
			return redirect('profiles:profile-update')
	else:
		form=RegistrationForm()
	return render(request,"accounts/signup.html",{'form':form})

@login_required()
def passchange(request):
	if request.method=='POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)
		if form.is_valid():
			form.save()
			messages.success(request,'Your Password Has Changed successfuly.')

			update_session_auth_hash(request,form.user)
			return redirect('post_app:index')
		else:
			messages.alert(request,'Please Correct the Info.')
			return redirect('accounts:passchange')	
	else:
		form=PasswordChangeForm(user=request.user)
	return render(request,'accounts/passchange.html',{'form':form})

@login_required()
def account_settings(request):
	if request.method=='POST':
		form=ChangeForm(data=request.POST or None,instance=request.user)
		# form2=ProfileForm(data=request.POST or None,instance=request.user.profile)
		if form.is_valid():
			form.save()
			messages.success(request,'Your Account Settings Has Changed successfuly.')
			return redirect('post_app:index')
	else:
		form=ChangeForm(instance=request.user)
	context={'form':form,}
	return render(request,'accounts/accounts_settings.html',context)	
