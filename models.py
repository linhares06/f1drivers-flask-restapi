from config import db

class Race(db.Model):
    """
    Represents a race in the Formula 1 database.

    Attributes:
    - race_id (int): Primary key for the 'races' table.
    - year (str): The year of the race.
    - name (str): The name of the race.
    - round (str): The round of the race.
    - results (relationship): One-to-many relationship with 'Results' table.

    Table Name: races
    """
    __tablename__ = "races"
    __table_args__ = {'extend_existing': True}
    race_id = db.Column(db.Integer, primary_key=True, name='raceId')
    year = db.Column(db.String(32))
    name = db.Column(db.String(32))
    round = db.Column(db.String(32))
    results = db.relationship('Results')

class Results(db.Model):
    """
    Represents results of a race in the Formula 1 database.

    Attributes:
    - result_id (int): Primary key for the 'results' table.
    - driver_id (int): Foreign key referencing 'driverId' in 'drivers' table.
    - race_id (int): Foreign key referencing 'raceId' in 'races' table.
    - grid (int): The starting grid position of the driver.
    - position (str): The finishing position of the driver in the race.
    - race (relationship): Many-to-one relationship with 'Race' table.

    Table Name: results
    """
    __tablename__ = "results"
    __table_args__ = {'extend_existing': True}
    result_id = db.Column(db.Integer, primary_key=True, name='resultId')
    driver_id = db.Column(db.Integer, name='driverId')
    race_id = db.Column(db.Integer, db.ForeignKey('races.raceId'), name='raceId')
    grid = db.Column(db.Integer)
    position = db.Column(db.String)
    race = db.relationship('Race', back_populates='results')

class Driver(db.Model):
    """
    Represents a driver in the Formula 1 database.

    Attributes:
    - driver_id (int): Primary key for the 'drivers' table.
    - driver_ref_name (str): Unique reference name for the driver.
    - number (str): The driver's racing number.
    - code (str): A three-letter code associated with the driver.
    - forename (str): The first name of the driver.
    - surname (str): The last name of the driver.
    - nationality (str): The nationality of the driver.
    - dob (str): The date of birth of the driver.

    Table Name: drivers
    """
    __tablename__ = "drivers"
    driver_id = db.Column(db.Integer, primary_key=True, nullable=False, name='driverId')
    driver_ref_name = db.Column(db.String(32), unique=True, nullable=False, name='driverRef')
    number = db.Column(db.String(32))
    code = db.Column(db.String(32))
    forename = db.Column(db.String(32), nullable=False)
    surname = db.Column(db.String(32), nullable=False)
    nationality = db.Column(db.String(32), nullable=False)
    dob = db.Column(db.String(10))