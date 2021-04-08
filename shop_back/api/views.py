from django.http.response import JsonResponse

from api.models import Product, Category


def products_list(request):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def categorys_list(request):
    caterogys = Category.objects.all()
    caterogys_json = [caterogy.to_json() for caterogy in caterogys]
    return JsonResponse(caterogys_json, safe=False)


def product_details(request, product_id):
    try:
        product=Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse( {
            'message':str(e),
            'error': f'Error finding the product with id {product_id}'
        })
    return JsonResponse(product.to_json())


def category_details(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse ({
            'message':str(e),
            'error': f'Error finding the category with id {category_id}'
        })
    return JsonResponse(category.to_json())
        