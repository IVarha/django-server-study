from django.conf.urls import include, url
from django.contrib import admin
import main_app.urls
print(str(dir(main_app)))
urlpatterns = [
    # Examples:
    url(r'^$', 'first_variant.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mainpage/', include(main_app.urls))
]
