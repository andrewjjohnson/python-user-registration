from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'meso_training.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('registration.urls'))
    url(r'^login/$', views.login, { 'template_name': 'login.html', 'authentication_form': LoginForm },)
]
