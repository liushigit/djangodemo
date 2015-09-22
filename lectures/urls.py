from django.conf.urls import include, url
from .views import LectureListView, LectureDetailView, LecturesByInstitution

urlpatterns = [
    url(r'^$', LectureListView.as_view(), name='lectures-index'),
    url(r'^(?P<pk>[0-9]+)$', LectureDetailView.as_view(), name='lecture-detail'),
    url(r'^institution/(?P<institution_id>[0-9]+)$',
        LecturesByInstitution.as_view(),
        name='lectures-institution'),
]
