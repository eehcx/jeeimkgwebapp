from functools import wraps
from django.shortcuts import redirect

def firebase_login_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        if 'uid' not in request.session:
            return redirect('login')
        return f(request, *args, **kwargs)
    return decorated_function


