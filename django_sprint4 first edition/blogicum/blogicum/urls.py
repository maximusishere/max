from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import include, path, reverse_lazy

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace='pages')),
    path('', include('blog.urls', namespace='blog')),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('blog:index'),
        ),
        name='registration',
    ),
]
