from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name='main'),
    path('new/', ShowAllPosts.as_view(), name='show_all_posts'),
    path('new/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<slug:cat_slug>/', Category.as_view(), name='category'),
    # path('portfolio/', PortfolioPage.as_view(), name='portfolio'),
    # path('price/', PricePage.as_view(), name='price'),
    # path('contacts/', ContactsPage.as_view(), name='contacts'),

    # path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    # path('category/<slug:cat_slug>/', BlogCategory.as_view(), name='category'),
    # path('portfolio_post/<slug:portf_slug>/', PortfolioPost.as_view(), name='portfolio_post'),
    # path('login/', LoginUser.as_view(), name='login_page'),
    # path('register/', RegisterUser.as_view(), name='register_page'),
    # path('logout/', LogoutUser.as_view(), name='logout_page'),
]