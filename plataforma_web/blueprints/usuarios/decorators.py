"""
Usuarios, decoradores
"""
from functools import wraps
from flask import abort, redirect
from flask_login import current_user


def anonymous_required(url='/'):
    """ Redirigir si ya se ha autentificado """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kargs):
            if current_user.is_authenticated:
                return redirect(url)
            return f(*args, **kargs)
        return decorated_function
    return decorator


def permission_required(perm):
    """ ¿Tiene permiso para estar en esta página? """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(perm):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator
