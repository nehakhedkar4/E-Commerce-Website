from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('index/',views.index,name='index'),


    path('',views.HomeView.as_view(),name='home'),
    path('<int:pk>',views.ProductDetailView.as_view(),name='product'),
    # path('delete/<int:pk>',views.AddDeleteView.as_view(),name="delete"),

    # path('cart/<int:pk>',views.AddToCartView.as_view(),name='cart'),
    path('address/',views.address,name='address'),
    # path('address/<int:pk>/',views.AddressView.as_view(),name='address'),
    # path('mobile/slug:data',views.mobile,name="mobiledata")
    # path('mobile/',views.mobile,name="mobiledata")
    # path('mobile/',views.MobilView.as_view(),name='mobiledata')

    path('addToCart/<int:pk>',views.addToCart,name='addToCart'),
    path('delete/<int:pk>',views.delete_item,name='delete'),

    # path("cart/<int:id>/increment/", views.increment, name="increment"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
