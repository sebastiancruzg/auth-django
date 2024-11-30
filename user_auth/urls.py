from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import login, sign_up, main_page


urlpatterns = [
    path('login/', login, name='login'),
    path('sign-up/' , sign_up),
    path('welcome/', main_page)
] + static(settings.STATIC_URL, document_root=settings.BASE_DIR)
