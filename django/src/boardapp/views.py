from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import BoardModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

def signupfunc(request):
#	user2 = User.objects.get(username='sasaki')
#	print(user2)
	if request.method == 'POST':
		username_input = request.POST['username']
		password_input = request.POST['password']
		try:
			User.objects.get(username=username_input)
			return render(request, 'signup.html', {'error':'This User already registered.'})
		except:
			user = User.objects.create_user(username_input, '', password_input)
			print(request.POST)
			return render(request, 'signup.html', {'some':100})
	return render(request, 'signup.html', {'some':100})


def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error':'Login Error.'})
#            return redirect('login',  {'error':'Login Error.'})
    return render(request, 'login.html')


@login_required
def listfunc(request):
	object_list = BoardModel.objects.all()
	return render(request, 'list.html', {'object_list':object_list})


def logoutfunc(request):
    logout(request)
    return redirect('login')


def detailfunc(request, pk):
	object = BoardModel.objects.get(pk=pk)
	return render (request, 'detail.html', {'object':object})


def goodfunc(request, pk):
	post = BoardModel.objects.get(pk = pk)
	post.good = post.good + 1
	post.save()
	return redirect('list')


def readfunc(request, pk):
	post = BoardModel.objects.get(pk = pk)
	uname = request.user.get_username()
	if uname not in post.readtext:
		post.read += 1
		post.readtext+=' ' + uname
		post.save()
	return redirect('list')


class BoardCreate(CreateView):
	template_name = 'create.html'
	model = BoardModel
	fields = ('title', 'content', 'author', 'images')
	success_url = reverse_lazy('list')

