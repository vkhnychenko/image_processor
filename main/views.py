from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import FormMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Image
from .forms import ImageForm, ImageDetailForm
from .services import resize_image


class ImageListView(ListView):
    model = Image
    template_name = 'main/index.html'


class ImageCreateView(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'main/create-image.html'


class ImageDetailView(FormMixin, DetailView):
    model = Image
    form_class = ImageDetailForm
    template_name = 'main/image_detail.html'

    def get_success_url(self):
        return reverse_lazy('main:image_detail', args=[self.get_object().id])

    def get_object(self):
        try:
            my_object = Image.objects.get(id=self.kwargs.get('pk'))
            return my_object
        except self.model.DoesNotExist:
            raise Http404("No MyModel matches the given query.")

    def get_context_data(self, **kwargs):
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            pillow_image = resize_image(self.object.image.path,
                                        width=form.cleaned_data['width'],
                                        height=form.cleaned_data['height'])
            img_name = 'image.jpg'
            self.object.update_image.save(img_name, InMemoryUploadedFile(
               pillow_image,
                None,
                img_name,
                'image/jpeg',
                pillow_image.tell,
                None))
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# class ImageUpdateView(UpdateView):
#     model = Image
#     form_class = ImageForm
#     template_name = 'main/image_detail.html'