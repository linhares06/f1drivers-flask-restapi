from flask import abort, make_response
from config import db
from models import Driver
from schemas import driver_schema, all_drivers_schema

def read_all():
    """
    Retrieve and return the serialized data for all F1 drivers.

    Returns:
    - dict: A dictionary containing serialized data for all F1 drivers.
    """
    drivers = Driver.query.all()
    return all_drivers_schema.dump(drivers)

def read_one(driver_ref_name):
    """
    Retrieve and return the serialized data for a specific F1 driver.

    Parameters:
    - driver_ref_name (str): The unique reference name of the F1 driver.

    Returns:
    - dict: A dictionary containing serialized data for the specified F1 driver.

    Raises:
    - 404 Error: If the F1 driver with the specified reference name is not found.
    """
    driver = Driver.query.filter(Driver.driver_ref_name == driver_ref_name).one_or_none()

    if driver is not None:
        return driver_schema.dump(driver)
    else:
        abort(404, f"F1 driver with reference name {driver_ref_name} not found")

def create(driver):
    """
    Create a new F1 driver based on the provided data.

    Parameters:
    - driver (dict): A dictionary containing data for creating a new F1 driver.

    Returns:
    - tuple: A tuple containing the serialized data for the new F1 driver and the HTTP status code (201 for created).

    Raises:
    - 406 Error: If an F1 driver with the specified reference name already exists.
    """
    driver_ref_name = driver.get("driver_ref_name")
    existing_driver = Driver.query.filter(Driver.driver_ref_name == driver_ref_name).one_or_none()

    if existing_driver is None:
        new_driver = driver_schema.load(driver, session=db.session)
        db.session.add(new_driver)
        db.session.commit()
        return driver_schema.dump(new_driver), 201
    else:
        abort(
            406,
            f"F1 driver with reference name {driver_ref_name} already exists"
        )

def update(driver_ref_name, driver):
    """
    Update an existing F1 driver with the provided data.

    Parameters:
    - driver_ref_name (str): The unique reference name of the F1 driver to be updated.
    - driver (dict): A dictionary containing data for updating the F1 driver.

    Returns:
    - tuple: A tuple containing the serialized data for the updated F1 driver and the HTTP status code (201 for updated).

    Raises:
    - 404 Error: If the F1 driver with the specified reference name is not found.
    - 406 Error: If another F1 driver with the updated reference name already exists.
    """
    existing_driver = Driver.query.filter(Driver.driver_ref_name == driver_ref_name).one_or_none()

    if existing_driver:
        driver_ref_name = driver.get("driver_ref_name")
        check_driver_ref_name = Driver.query.filter(Driver.driver_ref_name == driver_ref_name).one_or_none()

        if check_driver_ref_name is not None:
            abort(
                406,
                f"F1 driver with reference name {driver_ref_name} already exists"
            )
        else:  
            update_driver = driver_schema.load(driver, session=db.session)
            existing_driver.forename = update_driver.forename
            existing_driver.surname = update_driver.surname
            existing_driver.code = update_driver.code
            existing_driver.dob = update_driver.dob
            existing_driver.driver_ref_name = update_driver.driver_ref_name
            existing_driver.nationality = update_driver.nationality
            existing_driver.number = update_driver.number

            db.session.merge(existing_driver)
            db.session.commit()
            return driver_schema.dump(existing_driver), 201
    else:
        abort(404, f"F1 driver with reference name {driver_ref_name} not found")

def delete(driver_ref_name):
    """
    Delete an existing F1 driver with the specified reference name.

    Parameters:
    - driver_ref_name (str): The unique reference name of the F1 driver to be deleted.

    Returns:
    - Response: A response indicating the success of the deletion.

    Raises:
    - 404 Error: If the F1 driver with the specified reference name is not found.
    """
    existing_driver = Driver.query.filter(Driver.driver_ref_name == driver_ref_name).one_or_none()

    if existing_driver:
        db.session.delete(existing_driver)
        db.session.commit()
        return make_response(f"F1 driver {driver_ref_name} successfully deleted", 200)
    else:
        abort(404, f"F1 driver with reference name {driver_ref_name} not found")