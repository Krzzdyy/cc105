
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'student_management_sys/', include('student_management_sys.urls')),
    path('', include('student_management_sys.urls')),
]
