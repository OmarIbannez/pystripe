"""test_conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from payments.views import WebhokView, AddCreditCard, create_suscription, QuickPay
from webapp.views import Dashboard
from users.views import user_register


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', WebhokView.as_view(), name='webhok'),
    url(r'^add_credit_card/$', AddCreditCard.as_view(), name='add_credit_card'),
    url(r'^quick_pay/$', QuickPay.as_view(), name='quick_pay'),
    url(r'^create_suscription/$', create_suscription, name='create_suscription'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^register/$', user_register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
