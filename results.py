from flask import abort
from config import db
from models import Results, Race
from schemas import race_result_schema, race_schema, result_schema

def read_driver_results(driver_id):
    """
    Retrieve and return the serialized race results for a specific driver.

    Parameters:
    - driver_id (int): The unique identifier for the driver.

    Returns:
    - dict: A dictionary containing serialized race results for the specified driver.

    Raises:
    - 404 Error: If no results are found for the specified driver.
    """
    # Query the database to get the race results for the specified driver, ordered by year and round.
    query_results = (
        db.session.query(Results, Race)
        .join(Race, Results.race)
        .filter(Results.driver_id == driver_id)
        .order_by(Race.year, Race.round)
        .all()
    )
    
    # Extract results and race information from the query results and serialize the data.
    race_results = [
        {
            'results': result_schema.dump(result),
            'race': race_schema.dump(race)
        }
        for result, race in query_results
    ]

    # Check if any race results were found for the specified driver.
    if race_results != []:
        return race_result_schema.dump(race_results)
    else:
        # If no results are found, raise a 404 error with a custom message.
        abort(
            404, f"Results with driver ID {driver_id} not found"
        )