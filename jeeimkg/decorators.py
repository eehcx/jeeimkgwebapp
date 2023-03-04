"""   
from django.contrib.auth.decorators import user_passes_test
from auth_admin.views import is_authenticated_in_firebase

def firebase_auth_required(view_func):
    decorated_view_func = user_passes_test(
        is_authenticated_in_firebase,
        login_url='/login/'
    )(view_func)
    return decorated_view_func
"""