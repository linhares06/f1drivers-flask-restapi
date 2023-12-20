from config import ma, db
from models import Race, Results, Driver
from marshmallow_sqlalchemy import fields

class ResultSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing 'Results' model instances.
    """
    class Meta:
        model = Results

class RaceSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing 'Race' model instances.
    """
    class Meta:
        model = Race

class RaceResultSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing a combination of 'Result' and 'Race' model instances.
    """
    results = fields.Nested(ResultSchema)
    race = fields.Nested(RaceSchema)

class DriverSchema(ma.SQLAlchemyAutoSchema):
    """
    Schema for serializing and deserializing 'Driver' model instances.
    """
    class Meta:
        model = Driver
        load_instance = True
        sqla_session = db.session

# Instantiate schema objects for single instances and collections.
driver_schema = DriverSchema()
all_drivers_schema = DriverSchema(many=True)

result_schema = ResultSchema()
race_schema = RaceSchema()

# Schema for serializing and deserializing a combination of 'Result' and 'Race' model instances in a list.
race_result_schema = RaceResultSchema(many=True)