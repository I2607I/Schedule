from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('sc', SchView.as_view(), name='sc'),
    path('', HomeView.as_view(), name='home'),
    path('sc/<slug:parity_slug>/', SchParityView.as_view(), name='sc_parity'),
    path('subject/<slug:subject_slug>/', SubjectView.as_view(), name='subject'),
    # path('about/', about, name='about'),
    # path('cats/<int:catid>/', cat),
    # path('history/', history),
    # path('geography/', geography),
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive),
    # path('addpage', AddPage.as_view(), name='add_page'),
    # path('feedback', feedback, name='feedback'),
    # path('login', login, name='login'),
    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<slug:cat_slug>/', CharactersCategory.as_view(), name='category')
]
