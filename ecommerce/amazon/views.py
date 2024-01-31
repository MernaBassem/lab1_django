from django.shortcuts import render
from django.http import HttpResponse

products = [
 {
"id": 1,
"title": "iPhone 9",
"price": 549,
"category": "smartphones",
"thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",

},
{
"id": 2,
"title": "iPhone X",
"price": 899,
"category": "smartphones",
"thumbnail": "https://cdn.dummyjson.com/product-images/2/thumbnail.jpg",
},
{
"id": 3,
"title": "Samsung Universe 9",
"price": 1249,
"category": "smartphones",
"thumbnail": "https://cdn.dummyjson.com/product-images/3/thumbnail.jpg",
},
{
"id": 4,
"title": "OPPOF19",
"price": 280,
"category": "smartphones",
"thumbnail": "https://cdn.dummyjson.com/product-images/4/thumbnail.jpg",
},
{
"id": 5,
"title": "Huawei P30",
"price": 499,
"category": "smartphones",
"thumbnail": "https://cdn.dummyjson.com/product-images/5/thumbnail.jpg",

},
{
"id": 6,
"title": "MacBook Pro",
"price": 1749,
"category": "laptops",
"thumbnail": "https://cdn.dummyjson.com/product-images/6/thumbnail.png",
},
{
"id": 7,
"title": "Samsung Galaxy Book",
"price": 1499,
"category": "laptops",
"thumbnail": "https://cdn.dummyjson.com/product-images/7/thumbnail.jpg",
},
{
"id": 8,
"title": "Microsoft Surface Laptop 4",
"price": 1499,
"category": "laptops",
"thumbnail": "https://cdn.dummyjson.com/product-images/8/thumbnail.jpg",
},
{
"id": 9,
"title": "Infinix INBOOK",
"price": 1099,
"category": "laptops",
"thumbnail": "https://cdn.dummyjson.com/product-images/9/thumbnail.jpg",
},
{
"id": 10,
"title": "HP Pavilion 15-DK1056WM",
"price": 1099,
"category": "laptops",
"thumbnail": "https://cdn.dummyjson.com/product-images/10/thumbnail.jpeg",
},
{
"id": 11,
"title": "perfume Oil",
"price": 13,
"category": "fragrances",
"thumbnail": "https://cdn.dummyjson.com/product-images/11/thumbnail.jpg",
},
{
"id": 12,
"title": "Brown Perfume",
"price": 40,
"category": "fragrances",
"thumbnail": "https://cdn.dummyjson.com/product-images/12/thumbnail.jpg",

},
{
"id": 13,
"title": "Fog Scent Xpressio Perfume",
"price": 13,
"category": "fragrances",
"thumbnail": "https://cdn.dummyjson.com/product-images/13/thumbnail.webp",

},
{
"id": 14,
"title": "Non-Alcoholic Concentrated Perfume Oil",
"price": 120,
"category": "fragrances",
"thumbnail": "https://cdn.dummyjson.com/product-images/14/thumbnail.jpg",
},
{
"id": 15,
"title": "Eau De Perfume Spray",
"price": 30,
"category": "fragrances",
"thumbnail": "https://cdn.dummyjson.com/product-images/15/thumbnail.jpg",
},
{
"id": 16,
"title": "Hyaluronic Acid Serum",
"price": 19,
"category": "skincare",
"thumbnail": "https://cdn.dummyjson.com/product-images/16/thumbnail.jpg",
},
{
"id": 17,
"title": "Tree Oil 30ml",
"price": 12,
"category": "skincare",
"thumbnail": "https://cdn.dummyjson.com/product-images/17/thumbnail.jpg",

},
{
"id": 18,
"title": "Oil Free Moisturizer 100ml",
"price": 40,
"category": "skincare",
"thumbnail": "https://cdn.dummyjson.com/product-images/18/thumbnail.jpg",

},
{
"id": 19,
"title": "Skin Beauty Serum.",
"price": 46,
"category": "skincare",
"thumbnail": "https://cdn.dummyjson.com/product-images/19/thumbnail.jpg",

},
{
"id": 20,
"title": "Freckle Treatment Cream- 15gm",
"price": 70,
"category": "skincare",
"thumbnail": "https://cdn.dummyjson.com/product-images/20/thumbnail.jpg",

},
{
"id": 21,
"title": "- Daal Masoor 500 grams",
"price": 20,
"category": "groceries",
"thumbnail": "https://cdn.dummyjson.com/product-images/21/thumbnail.png",

},
{
"id": 22,
"title": "Elbow Macaroni - 400 gm",
"price": 14,
"category": "groceries",
"thumbnail": "https://cdn.dummyjson.com/product-images/22/thumbnail.jpg",

},
{
"id": 23,
"title": "Orange Essence Food Flavou",
"price": 14,
"category": "groceries",
"thumbnail": "https://cdn.dummyjson.com/product-images/23/thumbnail.jpg",

},
{
"id": 24,
"title": "cereals muesli fruit nuts",
"price": 46,
"category": "groceries",
"thumbnail": "https://cdn.dummyjson.com/product-images/24/thumbnail.jpg",

}
]

def product(request):
    context = {'products': products}
    return render(request, 'pages/product.html', context)

def productDetail(request, productID):
    product = next((p for p in products if p['id'] == productID), None)
    context = {'product': product}
    if product:
        return render(request, 'pages/productDetail.html', context)
    return HttpResponse('<span style="color:red">Product not found</span>')

def category(request):
    context = {'products': products}
    return render(request, 'pages/category.html', context)

def about(request):
    return render(request, 'pages/about.html')
