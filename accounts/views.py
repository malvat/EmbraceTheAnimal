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
        filled_form = AccountUserForm(request.POST)
        if filled_form.is_valid():
            try:
                user = AccountUser.objects.get(email=filled_form.cleaned_data.get("email"))
                user_form = AccountUserForm()
                return render(request, 'sign_up.html', {'form': user_form, 'note': 'user already exists'})
            except AccountUser.DoesNotExist:
                filled_form.save()
                user_form = AccountUserForm()
                return render(request, 'sign_in.html', {'form': user_form, 'note': 'Login to proceed'})
    else:
        user_form = AccountUserForm()
        return render(request, 'sign_up.html', {'form': user_form})
    

