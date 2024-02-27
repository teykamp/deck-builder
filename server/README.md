# Initial Setup
We are using python3.12. Ensure you have this version installed.
```bash
# Steps to install if python3.12 not present are TDB
```

Requires the packages `python3-django python3.12-venv python3.12-pip` installed on the system

Create your virtual environment and activate it with:
```bash
python3.12 -m venv venv
source deckbuilder_venv/bin/activate

# At any time to exit, you can type:
deactivate
```

Install project depenendencies:
```bash
pip install -r requirements.txt
```

Start the project, after setup is complete, by running:
```bash
python manage.py runserver
```

Once the server is running, navigate to `https://127.0.0.1:8000/hello` in a browser for 'hello world'.
