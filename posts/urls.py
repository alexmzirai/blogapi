from django.conf.urls import url

from . import views

'''all blog routes will be at api/ so our Postlist which has the empty string '' will be at /api
and post_urlDetail will be at api/# where # is the primary key of the entry
'''
urlpatterns = [
    url('', views.PostList.as_view()),
    url(r'^<int:pk>/', views.PostDetail.as_view()),
]

# all blog routes