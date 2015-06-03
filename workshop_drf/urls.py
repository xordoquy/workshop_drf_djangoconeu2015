from django.conf.urls import include, url
from django.contrib import admin
import workshop_drf.todo.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(workshop_drf.todo.urls)),
]

