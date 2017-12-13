from django.conf.urls import include, url
from sint import views


urlpatterns = [
        url(r'^$', views.base, name='base'),
        url(r'^contenido/$', views.contenido, name='contenido'),
        url(r'^category/$', views.category, name='category-list'),
        url(r'^category/(?P<category_id>\d+)/detail/$', views.category_detail,
                           name='category-detail'),
        url(r'^sujeto/$', views.sujeto, name='sujeto-list'),
        url(r'^sujeto/(?P<sujeto_id>\d+)/detail/$', views.sujeto_detail,
                           name='sujeto-detail'),

    ]
