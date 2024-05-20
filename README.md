This app demonstrates a basic CRUD application using Flask. Products are stored in a list and can be added, edited, and deleted. 
Images are uploaded to a directory, and the product list and forms are managed using Flask-WTF and WTForms.

# Application Structure 

my_flask_app/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── product_list.html
│   ├── product_form.html
└── static/
    └── uploads/
    
==========================================================================================
To run this app successfully, follow the below-mentioned steps
1: pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-WTF Flask-Uploads
2: python app.py
