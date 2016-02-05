from blog import views
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^bio/$', views.bio, name='bio'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<post_pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
    url(r'^post/(?P<post_pk>\d+)/comments/(?P<pk>\d+)/edit/$', views.comment_edit, name='comment_edit'),
    url(r'^category/$', views.category_list, name='category_list'),
    url(r'^tag/$', views.tag_list, name='tag_list'),
    url(r'^guest/$', views.guest_list, name='guest_list'),
    url(r'^guest/(?P<pk>\d+)/$', views.guest_detail, name='guest_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#url(r'^post/(?P<pk>\d+)/$', 'blog.views.post_detail')
#(?P:정규표현식으로 처리하겠다는 선언
#<pk>변수의 이름임. 뷰에서 받을 때도 <pk>라는 이름으로 받아야함.[primary key란 뜻, 다른 거 써도 되긴함.=각 데이터를 규정하는 유일한 아이디.]
#d가 오토필드, 프라이머리코드역할을 함.