from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('sc', SchView.as_view(), name='sc'),
    path('', HomeView.as_view(), name='home'),
    path('sc/<slug:parity_slug>/', SchParityView.as_view(), name='sc_parity'),
    path('subject/<slug:subject_slug>/', SubjectView.as_view(), name='subject'),
]
