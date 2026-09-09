from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from product.models import Product

def product_list(request):
    """Main sales page - shows products and cart"""
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    
    #Calculate cart total
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = Product.objects.filter(id=product_id).first()
        if product:
            item_total = product.price * quantity
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
            total += item_total

    context = {
        'products': products,
        'cart_items': cart_items,
        'cart_total': total,
    }
    return render(request, 'ventas/ventas.html', context)


def add_to_cart(request, product_id):
    """Add a product to the shopping cart"""
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    
    request.session['cart'] = cart
    messages.success(request, f'"{product.name}" added to cart.')
    return redirect('product_list')


def remove_from_cart(request, product_id):
    """Remove a product from the cart"""
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
        messages.info(request, 'Product removed from cart.')
    
    return redirect('product_list')


def process_order(request):
    """Process the order (simple version)"""
    cart = request.session.get('cart', {})
    
    if not cart:
        messages.warning(request, 'Your cart is empty.')
        return redirect('product_list')
    
    # Clear the cart after "ordering"
    request.session['cart'] = {}
    messages.success(request, 'Order processed successfully Thank you for your purchase.')
    return redirect('product_list')