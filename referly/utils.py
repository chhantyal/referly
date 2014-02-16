"""
All the reusable scripts are kept in this file
"""
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def get_object_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


class SetupViewMixin(object):
    """
    A mixin to to used when some basic setup work is needed to work with view.
    """
    def setup(self):
        pass

    def dispatch(self, request, *args, **kwargs):
        self.setup()
        return super(SetupViewMixin, self).dispatch(request, *args, **kwargs)