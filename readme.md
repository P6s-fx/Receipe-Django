# Receipe Tray

## Description

The Receipe Tray is a website for the delicious receipe collection. It allows Admin to Add, Delete or Modify recipes and users can view all available recipes. Back-end is developed Using Python-Django framework.

## Table of Contents

- [Project Structure](#Project_Structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)


## Project_Structure
```bash
Receipe-Django
    ├───accounts
    │   ├───migrations
    │   │   └───__pycache__
    │   └───__pycache__
    ├───Dweb
    │   └───__pycache__
    ├───home
    │   ├───migrations
    │   │   └───__pycache__
    │   ├───templates
    │   │   └───home
    │   └───__pycache__
    ├───public
    │   └───static
    │       └───recipes
    ├───recipes
    └───veggie
        ├───migrations
        │   └───__pycache__
        ├───templates
        └───__pycache__
```
## Features

The Restaurant Billing System project provides the following key features:

- User-friendly interface
- Storing Receipes in Database
- User can Add, modify and delete the receipe data

## Installation

To use the Restaurant Billing System, follow these installation steps:

1. Clone the repository

```bash
git clone https://github.com/<username>/<forked-repo>.git
```

2. Create your own virtual environment

Every time you start your machine, you must activate the virtual environment using source venv/bin/activate.

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install your requirements

```bash
pip install -r requirements.txt
```

5. Make your migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a new superuser

```bash
python manage.py createsuperuser
```

7. Final checks
Start the development server and ensure everything is running without errors.

```bash
python manage.py runserver
```

## Usage

- Launch the application using the installation steps mentioned above.
- Use the user-friendly interface to manage Receipe Information.
- Receipe data is stored in SQLite database

## Contributing

If you want to contribute to this project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and submit a pull request.
- Follow coding standards and conventions.
- Please report any issues or suggest improvements by creating an issue.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

We would like to acknowledge the following libraries and modules that made this project possible:

- HTML
- CSS
- Bootstrap
- Python
- Django Framework  
- SQLite database

## Contact

If you have questions or want to get in touch with the project maintainer, feel free to contact:

- Param Suthar
- Email: <param.corpid@email.com>
- Linkedin: [Linkedin/ParamSuthar](https://www.linkedin.com/in/paramsuthar)
- GitHub: [Github/P6s-fx](https://github.com/P6s-fx)
