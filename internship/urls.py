
# internship/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import internship_form_view, success_view

urlpatterns = [
    path('', internship_form_view, name='internship_form'),
    path('success/', success_view, name='success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    