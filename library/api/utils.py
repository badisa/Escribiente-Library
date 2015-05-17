from django.http import Http404


def getor404(manager, **kwargs):
    try:
        obj = manager.get(**kwargs)
    except manager.model.DoesNotExist:
        raise Http404
    return obj
