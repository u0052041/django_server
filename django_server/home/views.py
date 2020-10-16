from django.shortcuts import render
from django.core.cache import cache
import random
# Create your views here.


def home(request):
    test = cache.get("test")
    if not test:
        cache.set("test", random.randint(0, 1000), timeout=2)
    return render(request, "home.html", locals())