from . import shop
from flask import render_template, redirect, session, url_for, g, flash, request, json
from .forms import Order, AddItem
from .models import Item, Orders, Categories

NAME = 'misha'


@shop.route('/about/')
@shop.route('/')
def about():
    return render_template("about.html", name = NAME)


@shop.route('/main_page/')
def main_page():
    items = Item.objects[:20]
    return render_template("shop.html", items = items)

@shop.route('/item/<int:it_id>')
def item(it_id):
    item = Item.objects(item_id = it_id).first()
    return render_template("item.html", item = item)

@shop.route('/categories/')
def categories():
    cat_dict = {}
    for category in Categories.objects():
        item = Item.objects(category = category.name).first()
        cat_dict[category.name] = item.photo_hash
    return render_template("categories.html", cat_dict = cat_dict)

@shop.route('/category/<string:categ>')
def category(categ):
    items = Item.objects(category = categ)
    return render_template("category.html", items = items, category = categ)


@shop.route('/orders/', methods = ['GET', 'POST'])
def orders():
    order_form = Order()
    item_list = []

    items = []
    if 'items' in session:
        dat = session['items'].split()
        for it_id in dat:
            items.append(Item.objects(item_id = it_id).first())

    if order_form.validate_on_submit():
        if 'items' in session:
            dat = session['items'].split()
            for item_id in dat:
                item = Item.objects(item_id = item_id).first()
                item_list.append(item)
            order = Orders(
                            name = order_form.name.data, 
                            adress = order_form.adress.data,
                            description = order_form.description.data,
                            items_id = item_list
                          )
            order.save()
            session['items'] = ''

    return render_template("orders.html", items = items, form = order_form)


@shop.route('/add_item/', methods = ['GET', 'POST'])
def add_item():
    form = AddItem()
    if form.validate_on_submit():

        if Categories.objects(name = form.category.data):
            amount = (Categories.objects(name = form.category.data).first())['count']
            amount = int(amount)
            Categories.objects(name = form.category.data).update(count = str(amount+1))      

        else:
            categ = Categories(
                                name = form.category.data,
                                count = '1'
                                )
            categ.save()
        
        item = Item(
                    name = form.name.data,
                    cost = form.cost.data,
                    category = form.category.data,
                    description = form.description.data,
                    photo_hash = form.photo_hash.data
                    )
        item.save()
    return render_template("add_item.html", form = form)


@shop.route('/add_item_in_order/', methods = ['POST'])
def add_in_order():
    data = request.form['id']

    if 'items' in session:
        session['items'] += (data+' ')
        print('!!!')
    else:
        print('&&&')
        session['items'] = data
    return('success')
























    

    
