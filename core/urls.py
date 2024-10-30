"""
URL configuration for school_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from app.account.views import LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.account.urls')),
    path('student/',include('app.student.urls')),
    path('admission/',include('app.admission.urls')),
    path('fee/',include('app.fee.urls')),
    path('employee/',include('app.employee.urls'), name='employee'),
    path('payroll/',include('app.payroll.urls')),
    path('inventory/',include('app.inventory.urls')),
    path('finance/',include('app.finance.urls')),
    path('attendance/',include('app.attendance.urls')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('__reload__/', include('django_browser_reload.urls')),
    ] + urlpatterns
# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)