from django.shortcuts import render
from django.urls import reverse
from ndb_app.models import Product


import qrcode
from django.http import HttpResponse
from io import BytesIO

# Create your views here.
def index(request):
    produts=Product.objects.all()
    context={
        'products':produts
    }
    return render(request,'index.html',context)

def product_details(request,pk):
    product=Product.objects.get(id=pk)
    product={
        'product':product
    }
    return render(request,'product.html',product)

def generate_qr(request, url_path):
    # Example: url_path = 'ndb_app/perfumes/'
    full_url = request.build_absolute_uri(f'/{url_path.strip("/")}/')

    qr = qrcode.make(full_url)
    buffer = BytesIO()
    qr.save(buffer)
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type='image/png')

def qr_page(request):
    # The target URL you want the QR to link to (e.g., perfume category)
    target_url = reverse('index')  # use your real route name
    return render(request, 'qr_code.html', {'target_url': target_url})