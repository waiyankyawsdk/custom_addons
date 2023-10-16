from . import models
from . import wizard
from . import hooks
from . import controllers
from . import reporting

def post_init_hook(cr, registry):
    hooks.test_post_init_test(cr, registry)

def post_load():
    hooks.post_load_hook()
