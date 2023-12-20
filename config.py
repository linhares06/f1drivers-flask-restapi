import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Get the absolute path of the directory containing this script.
basedir = pathlib.Path(__file__).parent.resolve()

# Create a Connexion App instance with the current module as the name and the specification directory set to the script's directory.
connex_app = connexion.App(__name__, specification_dir=basedir)

# Extract the underlying Flask app from the Connexion App instance.
app = connex_app.app

# Configure the Flask app with a SQLite database URI and disable modification tracking.
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'f1drivers.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create a SQLAlchemy instance for database management.
db = SQLAlchemy(app)

# Create a Marshmallow instance for object serialization and deserialization.
ma = Marshmallow(app)