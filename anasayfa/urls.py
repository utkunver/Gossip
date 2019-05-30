from django.urls import path
from django.conf.urls import url

from .views import gundem_view,gossipozel_view,spor_view,edebiyat_view,hakkimizda_view,iletisim_view,detail_view,sinema_view

urlpatterns = [

    path('gundem/', gundem_view, name='gundem'),
    path('gossipözel/', gossipozel_view, name='gossipözel'),
    path('edebiyat/', edebiyat_view, name='edebiyat'),
    path('spor/', spor_view, name='spor'),
    path('sinema/', sinema_view, name='sinema'),
    path('hakkimizda/', hakkimizda_view, name='hakkimizda'),
    path('iletisim/', iletisim_view, name='iletisim'),
    url(r'(?P<id>\d+)/$', detail_view,name='detail'),

]