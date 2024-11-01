from flask import Flask, render_template, request
import dao

app = Flask(__name__)

@app.route('/')
def index():
    q = request.args.get("q")
    c_id = request.args.get("category")

    products = dao.load_products(q, c_id)
    categories = common_attributes()["categories"]  # Gọi hàm để lấy categories
    return render_template('index.html', categories=categories, products=products)

@app.route('/product/<int:id>')
def get_product(id):
    product = dao.load_product_by_id(id)
    return render_template('product.html', product=product)

@app.context_processor
def common_attributes():
    return {
        "categories": dao.load_categories()
    }

if __name__ == "__main__":
    app.run(debug=True)
