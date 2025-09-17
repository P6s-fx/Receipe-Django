# Recipe Tray 🍲

![Django](https://img.shields.io/badge/Django-4.2.9-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tailwind](https://img.shields.io/badge/Tailwind-CSS-38B2AC.svg)

## Description

Recipe Tray is a modern recipe management application built with Django. It allows users to create, browse, search, update, and delete recipes with an elegant, responsive UI powered by Tailwind CSS.

## Features

- 🎨 Clean, responsive UI with light/dark mode support
- 📝 Complete recipe management (CRUD operations)
- 🖼️ Image upload for recipes
- 🔒 User authentication system
- 🔍 Recipe search functionality
- 👑 Admin panel for advanced management

## Project Structure

```
Recipe Website (Django)/
├─ Dweb/                 # Django project configuration
├─ accounts/             # User account management
├─ home/                 # Public pages (home, about, contact)
├─ veggie/               # Recipes app (models, views, auth)
├─ public/               # Static assets
│  └─ static/            # CSS, JS, images
├─ db.sqlite3            # SQLite database
├─ manage.py             # Django management script
├─ requirements.txt      # Project dependencies
└─ readme.md             # This file
```

## Requirements

```
asgiref==3.7.2
Django==4.2.9
pillow==10.0.0
setuptools==68.0.0
sqlparse==0.4.4
wheel==0.41.2
```

Compatibility:
- Python 3.8+
- Django 4.2.9

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/P6s-fx/Receipe-Django.git
```

### 2. Set up a virtual environment

```bash
# Install virtualenv if you don't have it
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
# source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an admin user (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

The application will be available at:
- 🏠 Home: http://127.0.0.1:8000/
- 🍽️ Recipes: http://127.0.0.1:8000/recipes/
- ⚙️ Admin: http://127.0.0.1:8000/admin/

## Usage

1. **Register/Login**: Create an account or log in to access the recipes page
2. **Browse Recipes**: View all available recipes on the recipes page
3. **Search**: Use the search bar to find recipes by keyword
4. **Create**: Add a new recipe with name, description, and image
5. **Manage**: Update or delete your existing recipes
6. **Admin**: Access the admin panel at /admin for advanced management

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework used
- [Tailwind CSS](https://tailwindcss.com/) - For the responsive UI
- [SQLite](https://www.sqlite.org/) - Database engine

## Contact

- Param Suthar
- Email: <param.corpid@email.com>
- LinkedIn: [Linkedin/ParamSuthar](https://www.linkedin.com/in/paramsuthar)
- GitHub: [Github/P6s-fx](https://github.com/P6s-fx)
