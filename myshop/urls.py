from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('index/',views.index,name='index'),
    # path('add-to-cart/',views.addToCart,name='add-to-cart'),
    # path('product/<int:pk>',views.,name='product'),


    path('',views.HomeView.as_view(),name='home'),
    path('<int:pk>',views.ProductDetailView.as_view(),name='product'),
    path('cart/<int:pk>',views.AddToCartView.as_view(),name='cart'),
    # path('mobile/slug:data',views.mobile,name="mobiledata")
    # path('mobile/',views.mobile,name="mobiledata")
    # path('mobile/',views.MobilView.as_view(),name='mobiledata')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
