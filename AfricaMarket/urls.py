"""AfricaMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.urls import include
from users import views as users_view
from django.conf.urls.static import static
import paypal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sellerdashboard/', users_view.seller_dashboard,name='seller-dashboard'),
    path('registerbuyer/', users_view.register_a_buyer,name='register-buyer'),
    path('registerseller/', users_view.register_a_seller,name='register-seller'),
    path('loginseller/', auth_views.LoginView.as_view(template_name='amweb/login_seller.html'),name='login_seller'),
    path('loginbuyer/', auth_views.LoginView.as_view(template_name='amweb/login_buyer.html'),name='login_buyer'),
    path('buyerprofile/', users_view.buyer_profile,name='buyer-profile'),
    path('sellerprofile/', users_view.seller_profile,name='seller-profile'),
    path('buyerprofileupdate/', users_view.buyer_profile_update,name='buyer-profile-update'),
    path('sellerprofileupdate/', users_view.seller_profile_update,name='seller-profile-update'),
    path('logoutseller/', auth_views.LogoutView.as_view(template_name='amweb/logout_seller.html'),name='logout_seller'),
    path('logoutbuyer/', auth_views.LogoutView.as_view(template_name='amweb/logout_buyer.html'),name='logout_buyer'),
    path('shelfoneupdate/', users_view.shelfone_update, name='shelfone-update'),
    path('shelftwoupdate/', users_view.shelftwo_update, name='shelftwo-update'),
    path('shelfthreeupdate/', users_view.shelfthree_update, name='shelfthree-update'),
    path('shelffourupdate/', users_view.shelffour_update, name='shelffour-update'),
    path('shelffiveupdate/', users_view.shelffive_update, name='shelffive-update'),
    path('paystack/',include('paystack.frameworks.django.urls')),
    path('paypals/',include('paypal.standard.ipn.urls')),
    path('', include('amweb.urls')),
    path('', include('inventory.urls')),
    ]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)