# Backend Bible Verse App

This repository contains the backend code for the Bible Verse App project. The backend is built using Flask, SQLAlchemy, and Flask-Migrate to manage database migrations.

## Getting Started
Follow these steps to set up the project locally:

### Prerequisites
Python 3.11 or later
Virtual environment (optional but recommended)
Git

### Installation
1. Clone the repository:

```bash
git clone https://github.com/YourUsername/Backend_Bible_Verse_App.git
cd Backend_Bible_Verse_App
```

2. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

### Configuration

1. Copy the sample .env.sample file and rename it to .env:

```bash
cp .env.sample .env
```

2. Edit the .env file to add your configuration values (e.g., API keys, database URL).

### Generate Secret Key

Run the following code to generate a secret key for your Flask app:

```bash
python generate_key.py
```

Copy the generated key and replace the placeholder SECRET_KEY value in your .env file.

### Initialize Database

1. Create the initial migration:

```bash
flask db init
```

2. Apply the migration to create the database tables:

```bash

flask db migrate
flask db upgrade
```

### Running the App
Start the development server:

```bash
flask run
```

Visit http://127.0.0.1:5000/ in your browser to access the app.

## Additional Information

For more details about the project, routes, and functionality, please refer to the code and comments in the files.

## Contributors
Hannah Watkins, Sarah Watkins

## License
This project is licensed under the MIT License.