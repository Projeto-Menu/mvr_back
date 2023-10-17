from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import render


from .models import Usuario
from .forms import FormUsuario

# Create your views here.

class CriaUsuario(CreateView):
    model = Usuario
    form_class = FormUsuario
    template_name = 'cadastro.html'
    # success_url = '/'
    
    def get_usuario(request):
    # if this is a POST request we need to process the form data
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = CriaUsuario(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect("/valeu/")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = CriaUsuario()

        return render(request, "name.html", {"form": form})
    
