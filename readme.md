# Recipe Tray

## Description

Recipe Tray is a simple, modern recipe manager built with Django. Admins can add, update, and delete recipes; authenticated users can browse and search. The UI is responsive and inspired by iOS, implemented with Tailwind CSS via CDN.

## Table of Contents

- [Project Structure](#project_structure)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)


## Project_structure
```bash
Receipe-Django/
  ├─ Receipe-Django/
  │  ├─ Dweb/                 # Django project (settings, urls, wsgi)
  │  ├─ accounts/             # (present, currently unused)
  │  ├─ home/                 # Public pages (home/about/contact)
  │  ├─ veggie/               # Recipes app (models, views, auth)
  │  ├─ public/static/        # Static assets (images)
  │  ├─ db.sqlite3            # SQLite database (dev)
  │  └─ manage.py
  └─ readme.md
```

## Features

- Modern, responsive UI (Tailwind) with light/dark support
- Recipes CRUD (create, list, search, update, delete)
- Image upload for each recipe
- Authentication (register, login, logout)
- Admin panel for advanced management

## Requirements

From `requirements.txt`:

```text
asgiref==3.9.1
Django==5.2.6
pillow==11.3.0
setuptools==80.9.0
sqlparse==0.5.3
wheel==0.45.1
```

Compatibility:
- Python 3.13+
- Django 5.1+ (project currently uses 5.2.6)

## Installation

1) Clone and enter the project directory
```bash
git clone https://github.com/<username>/<forked-repo>.git
cd Receipe-Django/Receipe-Django
```

2) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
```

3) Install dependencies
```bash
pip install -r requirements.txt
```

4) Apply database migrations
```bash
python manage.py migrate
```

5) (Optional) Create an admin user
```bash
python manage.py createsuperuser
```

6) Run the development server
```bash
python manage.py runserver
```

Visit:
- Home: http://127.0.0.1:8000/
- Recipes: http://127.0.0.1:8000/recipes/
- Admin: http://127.0.0.1:8000/admin/

## Usage

- Use Register/Login to access the recipes page.
- Add a recipe with a name, description, and image.
- Search by keyword on the recipes page.
- Update or delete existing recipes.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes and open a PR
4. Follow coding standards and include concise descriptions

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Python, Django
- Tailwind CSS (via CDN in templates)
- SQLite (development database)

## Contact

- Param Suthar
- Email: <param.corpid@email.com>
- Linkedin: [Linkedin/ParamSuthar](https://www.linkedin.com/in/paramsuthar)
- GitHub: [Github/P6s-fx](https://github.com/P6s-fx)
