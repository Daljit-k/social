from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^photo_home.html$', views.index,name='index'),
    url(r'^photo_profile.html$', views.profile,name='profile'),
    url(r'^photo_explore.html$', views.explore,name='explore'),
    url(r'^photo_upload.html$', views.upload,name='upload'),
    url(r'^photo_stories.html$', views.stories,name='stories'),
    url(r'^login.html$', views.log,name='login'),
    url(r'^signup.html/$', views.sign,name='signup'),
    url(r'^logout/$', views.logout,name='logout'),
    url(r'showimage/$', views.img,name='showimg'),
    url(r'^signup - 2.html/$', views.signup2,name='signup2'),
    url(r'^sendrequest/(?P<sr>[0-9]+)$', views.sendreq,name='sendreq'),
    url(r'^acceptrequest/$', views.acceptreq,name='acceptreq'),
    url(r'^comment/$', views.comment,name='comment'),
    
]
