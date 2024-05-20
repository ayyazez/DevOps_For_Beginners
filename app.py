from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

products = []

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    image = FileField('Product Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('product_list.html', products=products)

@app.route('/product/new', methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        image_file = form.image.data
        filename = secure_filename(image_file.filename)
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        new_product = {
            'id': len(products) + 1,
            'name': form.name.data,
            'price': form.price.data,
            'image': filename
        }
        products.append(new_product)
        flash('Product created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('product_form.html', form=form)

@app.route('/product/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if product is None:
        flash('Product not found!', 'danger')
        return redirect(url_for('index'))
    
    form = ProductForm(data=product)
    if form.validate_on_submit():
        if form.image.data:
            image_file = form.image.data
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            product['image'] = filename
        product['name'] = form.name.data
        product['price'] = form.price.data
        flash('Product updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('product_form.html', form=form)

@app.route('/product/delete/<int:id>', methods=['POST'])
def delete_product(id):
    global products
    products = [p for p in products if p['id'] != id]
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
