# Initial Setup
We are using python3.12. Ensure you have this version installed.
Requires the packages `python3.12-venv python3.12-pip` installed on the system on Debian

Create your virtual environment and activate it with:
```bash
python3.12 -m venv venv

source venv/bin/activate        # If on *nix
source venv/Scripts/activate    # If on Windows

# At any time to exit, you can type:
deactivate
```

Install project depenendencies:
```bash
pip install -r requirements.txt
```

The database access relies on several environment variables set. Create a `.env` file and add the contents:
```bash
export DB_NAME='<db name>'
export DB_USER='<db user>'
export DB_PASS='<db pass>'
export DB_HOST='<db host>'
export DB_PORT='<db port>'
```

Then update your shells environment variables with:
```bash
source .env
```
Verify the variables are present with: `echo $DB_NAME`


Start the project, after setup is complete, by running:
```bash
python manage.py runserver
```

Once the server is running, navigate to `https://127.0.0.1:8000` in a browser to test the application.
