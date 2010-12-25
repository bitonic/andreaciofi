from pylons import session, url, request
from pylons.controllers.util import redirect, abort
from decorator import decorator

def authorize():
    def validator(func, *args, **kwargs):
        if 'logged_in' not in session:
            abort(403)
        else:
            return func(*args, **kwargs)

    return decorator(validator)
