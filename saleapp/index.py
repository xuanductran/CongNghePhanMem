from flask import render_template, request,redirect
import dao
from saleapp import app


@app.route('/')
def index():
    q = request.args.get("q")
    cate_id = request.args.get("category_id")
    products = dao.load_products(q=q, cate_id=cate_id)
    print("cate : "+ cate_id)
    return render_template('index.html', products=products)


@app.route('/products/<int:id>')
def details(id):
    product = dao.load_product_by_id(id)
    return render_template('product-details.html', product = product)

@app.route('/login',methods=['get','post'])
def login_user():
    if(request.method.__eq__("POST")):
        print(request.form)
        name = request.form.get("user")
        password = request.form.get("password")
        if(name.__eq__("admin") and password.__eq__("123")):
            return redirect('/')
    return render_template('login.html',)



@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)