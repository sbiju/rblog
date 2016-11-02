from django.conf.urls import url
from .views import (
    UserListView,
    profile_view,
    profile_edit,
    contact_us,
    AboutUs,
)


urlpatterns = [

    url(r'^contact/$', contact_us, name='contact_us'),
    url(r'^about/$', AboutUs.as_view(), name="about_us"),
    url(r'^user/$', UserListView.as_view(), name="user_list"),
    url(r'^profile/edit/$', profile_edit, name='profile_update'),
    url(r'^profile/(?P<username>[\w.@+-]+)$', profile_view, name='profile'),

]