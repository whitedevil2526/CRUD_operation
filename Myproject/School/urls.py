from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from School import views

urlpatterns = [
    path('',views.home, name='home'),
    path('shoe/update/<int:shoe_id>/', views.update_shoe, name='update_shoe'),
    path('shoe/delete/<int:shoe_id>/', views.delete_shoe, name='delete_shoe'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
