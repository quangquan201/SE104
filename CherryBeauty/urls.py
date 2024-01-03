from django.forms import forms
from django.urls import path
from . import views
from .views import AddComment

#urlcof
urlpatterns = [
    path('base/', views.base, name="base"),
    path('', views.home_page, name="home"),
    path('search/',views.searchpage, name ="search"),
    path('aboutus/',views.about_us, name="aboutus"),
    path('support/',views.support, name="support"),
    path('register/',views.register, name="register"),
    path('login/',views.log_in, name="login"),
    path('logout/',views.logoutUser, name = "logout"),
    path('blog/',views.blog_page, name="blog"),
    path('like/<slug:slug>/',views.LikeView,name="like_post"),
    path('product/',views.product_page, name ="product"),
    path('makeup/',views.makeuppage, name ="makeup"),
    path('skincare/',views.skincarepage, name ="skincare"),  
    path('brand/',views.brand,name="brand"),
    path('cart/',views.cartpage,name="cart"),
    path('checkout/',views.checkoutpage,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('userinfo/',views.userPage,name="userpage"),
    path('acticle/<slug:slug>/comment',AddComment.as_view(),name="add_comment"),
    path('sanpham/<slug:item_slug>/',views.item_detail,name="item_detail"),
    path('blog/<slug:slug>/',views.article_detail,name="article_detail"),
]

