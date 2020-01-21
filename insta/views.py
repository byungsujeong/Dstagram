from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from insta.models import Photo

# Create your views here.
def list(request):
    data = Photo.objects.all()
    list = {'list':data}
    return render(request, 'insta/list.html', list)

class PhotoUpload(CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'insta/upload.html'

    def form_valid(self, form):
        form.instance.author_id = 1

        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDetail(DetailView):
    model = Photo
    template_name = 'insta/detail.html'