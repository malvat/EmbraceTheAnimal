from django.shortcuts import redirect, render

def home(request): 
    if "logged_in" in request.session.keys(): 
        print(request.session['logged_in'])
        return render(request, 'home.html', {
            'logged_in': request.session['logged_in']
        })
    else:
        return render(request, 'home.html', {
            'logged_in': False
        })