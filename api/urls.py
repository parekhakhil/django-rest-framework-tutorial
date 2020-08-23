from django.urls import path,re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView,DetailsView ,UserView,UserDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    re_path(r'^bucketlists/$', CreateView.as_view(), name="create"),
    re_path(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details"),
    path('users/', UserView.as_view(), name="users"),
    re_path(r'users/(?P<pk>[0-9]+)/$',
        UserDetailsView.as_view(), name="user_details"),
    path('get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)


