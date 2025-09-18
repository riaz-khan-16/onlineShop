from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'webcontent', WebContentViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home, name='home'),
    path('product/<int:product_id>/',productDetails, name='productDetails' ),
    path('demo/<int:product_id>/',productDemo, name='productDemo' ),

    #crud for product
    path('product_list', productList.as_view(), name='productList' ),
    path('add_product',addProduct.as_view(), name='addProduct' ),
    path('update_product/<int:pk>',UpdateProduct.as_view(), name='UpdateProduct' ),
    path('delete_product/<int:pk>',deleteProduct.as_view(), name='deleteProduct' ),


    #crud for category

    path('category_list', categoryList.as_view(), name='categoryList' ),
    path('add_category', categoryAdd.as_view(), name='categoryAdd'),
    path('update_category/<int:pk>',UpdateCategory.as_view(), name='UpdateCategory' ),
    path('delete_category/<int:pk>',deleteCategory.as_view(), name='deleteCategory' ),


    #crud for WebContent

    path('webcontents', WebContentList.as_view(), name='WebContentList' ),
    path('add_webcontent',  WebContentAdd.as_view(), name='WebContentAdd'),
    path('update_webcontents/<int:pk>',UpdateWebContent.as_view(), name='UpdateWebContent' ),
    path('delete_webcontents/<int:pk>',deleteWebContent.as_view(), name='deleteWebContent' ),



    #crud for shop
    path('shop_list', shopList.as_view(), name='shopList' ),
    path('add_shop',shopAdd.as_view(), name='shopAdd' ),
    path('update_shop/<int:pk>',shopUpdate.as_view(), name='shopUpdate' ),
    path('delete_shop/<int:pk>',shopDelete.as_view(), name='shopDelete' ),


    # admin
    path('admin_dashboard', adminPanel, name='adminPanel' ),











    
]
