from django.shortcuts import render 
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Shortener
from .forms import ShortenerForm

def home_view(request):
    template = 'urlShortener/home.html'
    context = {}
    context['form'] = ShortenerForm()
    if request.method == 'GET':
        return render(request, template, context)
    elif request.method == 'POST':
        used_form = ShortenerForm(request.POST)
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.newURL
            originalURL = shortened_object.originalURL 
            context['new_url']  = new_url
            context['originalURL'] = originalURL
            return render(request, template, context)

        context['errors'] = used_form.errors
        return render(request, template, context)
        
def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(newURL=shortened_part)
        shortener.save()
        return HttpResponseRedirect(shortener.originalURL)
    except:
        raise Http404('Broken link')