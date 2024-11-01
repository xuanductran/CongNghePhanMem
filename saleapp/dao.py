import json


def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        categories = json.load(f)

        return categories

def load_products(q=None,c_id=None):
    with open('data/products.json', encoding='utf-8') as f:
        products = json.load(f)
        if q:
            products = [p for p in products if q.lower() in p["name"].lower()]
        if c_id:
            products = [p for p in products if int(c_id) == p["category_id"]]

        return products

def load_product_by_id(id):
    with open('data/products.json', encoding='utf-8') as f:
        products = json.load(f)
        for p in products:
            if(p["id"]==id):
                return p

if __name__=="__main__":
    print(load_products())