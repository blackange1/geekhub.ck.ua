from django.conf import settings
from django.shortcuts import render, redirect
from .models import CategoryOfGuitar, Guitar, Basket
from django.shortcuts import render, redirect

from .models import CategoryOfGuitar, Guitar, Basket


def index(request):
    context = {
        'title': 'guitar world',
        'guitars': Guitar.objects.all(),
        'category': CategoryOfGuitar.objects.all(),
    }
    return render(request, 'goods/index.html', context=context)


def profile(request):
    return redirect('index')


def logout(request):
    request.session.clear()
    return redirect('index')


def category(request, id_category):
    context = {
        'title': 'guitar world',
        'guitars': CategoryOfGuitar.objects.get(pk=id_category).guitar_set.all(),
        'category': (CategoryOfGuitar.objects.get(pk=id_category),),
    }
    return render(request, 'goods/index.html', context=context)


def product(request, id_product):
    context = {
        'guitar': Guitar.objects.get(pk=id_product),
    }
    return render(request, 'goods/product.html', context=context)


# http://127.0.0.1:8000/product/edit/1/
def edit_product(request, id_product):
    if not request.user.is_superuser:
        return redirect('index')

    def get_status(req):
        guitar.title = req.get('title', '')
        guitar.price = req.get('price', '')
        category = req.get('category', '')
        guitar.description = req.get('description', '')
        guitar.count = req.get('count', '')
        if guitar.title == '':
            return 'название не может бить пустим', 'danger'
        if not guitar.price.isdigit():
            return 'что не так с ценой', 'danger'
        if not guitar.count.isdigit():
            return 'что не так с количеством', 'danger'
        all_guitar = CategoryOfGuitar.objects.all()
        if category.isdigit():
            category = int(category)
            if not (category in all_guitar.values_list('id', flat=True)):
                return 'нет такой категории', 'danger'
            guitar.products_id = int(category)
        guitar.save()
        return 'даные сохранены', 'primary'

    message = ''
    class_alert = ''
    guitar = Guitar.objects.get(pk=id_product)
    if request.method == 'POST':
        message, class_alert = get_status(request.POST)

    context = {
        'guitar': guitar,
        'category': CategoryOfGuitar.objects.all(),
        'message': message,
        'class_alert': class_alert,
    }
    return render(request, 'goods/edit_product.html', context=context)


# http://127.0.0.1:8000/product/delete/1/
def delete_product(request, id_product):
    if not request.user.is_superuser:
        return redirect('index')
    Guitar.objects.get(pk=id_product).delete()
    for obj in Basket.objects.filter(product_id=id_product):
        obj.delete()
    return redirect('index')


def basket(request, id_user):
    if request.user.id != id_user:
        return redirect('index')
    guitars = []
    for basket in Basket.objects.filter(user_id=id_user):
        g = Guitar.objects.get(id=basket.product_id)
        g.id_basket = basket.id
        guitars.append(g)
    context = {
        'guitars': guitars,
    }
    return render(request, 'goods/basket.html', context=context)


# product/add_product_to_basket/1/
def add_product_to_basket(request, id_product):
    user = request.user
    if user.id:
        Basket.objects.create(
            user_id=user.id,
            product_id=id_product,
        ).save()
    return redirect('index')


def delete_product_with_basket(request, id_basket):
    if request.user.id:
        Basket.objects.get(id=id_basket).delete()
        return redirect('basket', id_user=request.user.id)
    return redirect('index')
