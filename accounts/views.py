from django.shortcuts import render
from django.shortcuts import render
from django.http import Http404
from .models import AccountUser
from .forms import AccountUserForm

def sign_in(request): 
    user_form = AccountUserForm()
    if request.method == "POST":
        # try: 
            print(request.POST['email'], request.POST['password'])
            user = AccountUser.objects.all()
            print(user)
            request.session['logged_in'] = True
            return render(request, 'home.html')
        # except AccountUser.DoesNotExist:
            # request.session['logged_in'] = False
            # return render(request, 'sign_in.html', {'form': user_form, 'note': 'please try again'})
    else:
        if 'logged_in' in request.session.keys():
            if request.session['logged_in']:
                return render(request, 'home.html')
        return render(request, 'sign_in.html', {'form': user_form})

def sign_up(request):
    if request.method == "POST" :
        try:
            user = AccountUser.objects.get(email=request.POST['email'])
            return render(request, 'sign_up.html', {'note': 'user already exists'})
        except AccountUser.DoesNotExist:
            tmp_user = AccountUser.objects.create(email=request.POST['email'], 
            password=request.POST['password'], 
            first_name=request.POST['first_name'], 
            last_name=request.POST['last_name'])
            tmp_user.save() 
            return render(request, 'sign_in.html', {'note': 'Login to proceed'})
    else:
        return render(request, 'sign_up.html')
    

