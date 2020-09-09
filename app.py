from os.path import join, abspath, dirname
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/img/products'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    img = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text)

    def __repr__(self):
        return self.title


@app.route('/')
@app.route('/home')
def index_page():
    return render_template("index.html")


@app.route('/catalog')
def catalog_page():
    products = Product.query.order_by(Product.id).all()
    return render_template("catalog.html", products=products)


@app.route('/product-<int:id>')
def product_page(id):
    product = Product.query.get(id)
    return render_template("product.html", product=product)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/create', methods=['POST', 'GET'])
def create_database_post():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        text = request.form['text']

        file = request.files['img']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            basedir = join(abspath(dirname(__file__)), app.config['UPLOAD_FOLDER'])
            file.save(join(basedir, filename))
            img = join('img/products/', filename)

            product = Product(title=title, price=price, img=img, text=text)

            try:
                db.session.add(product)
                db.session.commit()
                return redirect('/')
            except:
                return "Error"

    return render_template("create.html")


if __name__ == '__main__':
    app.run(debug=True)
