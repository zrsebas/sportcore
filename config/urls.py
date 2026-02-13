from django.contrib import admin
from django.urls import path, include
from sportcore_app.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include('sportcore_app.urls')),
]
