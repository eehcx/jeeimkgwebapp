from django.shortcuts import redirect

def firebase_login_required(function):
    def wrapper(request, *args, **kwargs):
        if 'email' in request.session:
            return function(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper


