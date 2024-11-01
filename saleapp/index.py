from flask import Flask, render_template,request
import dao


app = Flask(__name__)

@app.route('/')
def index():
    q=request.args.get("q")
    c_id=request.args.get("category")
    categories = dao.load_categories(c_id)
    products = dao.load_products(q,c_id)
    return render_template('index.html', categories=categories, products=products)

@app.route('/product/<int:id>')
def get_product(id):

    return render_template('product.html')


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)