from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
import requests
from .models import Shop, WebContent, Product, Category
from .serializers import ShopSerializer, WebContentSerializer, ProductSerializer, CategorySerializer
from .forms import ProductForm

# Create your views here.
def MakeSuperUser(request):
    user=User.objects.create_superuser(username="riaz", password="riaz1234@", email="riaz@gmail.com")
    user.save()

    return HttpResponse("User Created Successfully!")


#APIS
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class WebContentViewSet(viewsets.ModelViewSet):
    queryset = WebContent.objects.all()
    serializer_class = WebContentSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



#views


def home(request):
    return render(request,'product.html')

def productDetails(request, product_id):
    return render(request, "product_details.html", {"product_id": product_id})

def productDemo(request, product_id):
    return render(request, "demo.html", {"product_id": product_id})



#CRUD for Product

#CRUD using function based view


# def productList(request):
#     products = Product.objects.all()
#     return render(request, "product/product_list.html", {"products": products})


#write

# def addProduct(request):
#     if request.method=='POST':
#         form=ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("productList")
#     else:
#             form = ProductForm()
#     return render(request, "product/add_product.html", {"form": form, "title": "Add Product"})



#update is same like write but small different

# def UpdateProduct(request, pk):
#     product=get_object_or_404(Product, pk=pk)
#     if request.method=='POST':
#         form=ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("productList")
#     else:
#             form = ProductForm(instance=product)
#     return render(request, "product/add_product.html", {"form": form, "title": "Add Product"})


#delete

# def deleteProduct(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     print(product.id)
#     if request.method=='GET':
#         product.delete()
#         return redirect("productList")
    
#     return render(request, "product/product_list.html",  {"product": product})



#using Generic View


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *

#CRUD for Product
class productList(ListView):
    model = Product
    template_name = "product/product_list.html"
    context_object_name = "products"

class addProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/add_product.html"
    success_url = reverse_lazy("productList")

class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/add_product.html"
    success_url = reverse_lazy("productList")


class deleteProduct(DeleteView):
    model = Product
    template_name = "product/product_delete.html"
    success_url = reverse_lazy("productList")



#CRUD for Category
class categoryList(ListView):
    model = Category
    template_name = "category/category_list.html"
    context_object_name = "categories"


class categoryAdd(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/category_add.html"
    success_url = reverse_lazy("categoryList")

class UpdateCategory(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/category_add.html"
    success_url = reverse_lazy("categoryList")

class deleteCategory(DeleteView):
    model = Category
    template_name = "category/category_delete.html"
    success_url = reverse_lazy("categoryList")




#CRUD for Web Content
class WebContentList(ListView):
    model = WebContent
    template_name = "webcontent/webcontent_list.html"
    context_object_name = "webcontents"

class WebContentAdd(CreateView):
    model =WebContent
    form_class = WebContentForm
    template_name = "webcontent/webcontent_add.html"
    success_url = reverse_lazy("WebContentList")

class UpdateWebContent(UpdateView):
    model = WebContent
    form_class = WebContentForm
    template_name = "webcontent/webcontent_add.html"
    success_url = reverse_lazy("WebContentList")

class deleteWebContent(DeleteView):
    model = WebContent
    template_name = "webcontent/webcontent_delete.html"
    success_url = reverse_lazy("WebContentList")




#CRUD for Web Content
class shopList(ListView):
    model = Shop
    template_name = "shop/shop_list.html"
    context_object_name = "shops"

class shopAdd(CreateView):
    model =Shop
    form_class = shopForm
    template_name = "shop/add_shop.html"
    success_url = reverse_lazy("shopList")

class shopUpdate(UpdateView):
    model = Shop
    form_class = shopForm
    template_name = "shop/add_shop.html"
    success_url = reverse_lazy("shopList")

class shopDelete(DeleteView):
    model = Shop
    template_name = "shop/delete_shop.html"
    success_url = reverse_lazy("shopList")




#admin

def adminPanel(request):
    return render(request, "admin/dashboard.html")