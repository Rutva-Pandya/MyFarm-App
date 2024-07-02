# MyFarm App

This app is intended to be a farm management system that provides users with an interface to navigate and monitor their field along with providing a GPT-4 Vision powered assistant, CropWizard.

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation & Setup

Instructions on how to install and set up the project.

This project is hosted on the NCSA AIFarms Cluster and can be accessed by users with the required privileges. To start the Django server hosting the app, follow these steps:

1. Navigate to the project directory:
    ```bash
    cd /home/rutvadp2/MyFarm-App/MyFarm
    ```

2. Run the Django server:
    ```bash
    python3 manage.py runserver
    ```

With this, the server should be hosted on [http://127.0.0.1:5001/](http://127.0.0.1:5001/).

## Usage

This app is developed using Django and has multiple sub apps (CropWizard, Farm_View, Home, etc...) that can be individually developed and tested. 

Within each app, the frontend is managed in the static (used for CSS & JavaScript files) and templates (used for HTML files) folders. Any changes made to the interface will be managed in these directories and will automatically be updated on the Django server hosting the MyFarm App.