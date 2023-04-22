from functools import wraps
from django.shortcuts import redirect

def require_authentication(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        # Verificar si el usuario está autenticado
        if 'user_id' not in request.session:
            return redirect('login')

        # Si el usuario está autenticado, ejecutar la vista
        return view_func(request, *args, **kwargs)

    return wrapper

