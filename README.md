# F1 Drivers API Project
This project is a Python-based RESTful API with Flask that provides information about Formula 1 drivers.
It uses Flask, Connexion for API specification and routing, SQLAlchemy for integration with a relational database,
and Swagger/OpenAPI for endpoint documentation.

## Running 
1. Clone repository.
2. pip install requirements.txt
4. Start server by running python app.py

## API Documentation
Swagger UI documentation at [http://localhost:8000/api/ui/](http://localhost:8000/api/ui/) to interactively explore and test the API endpoints.

## Endpoints
- **GET /drivers:** Retrieve a list of all F1 drivers.
- **POST /drivers:** Add a new F1 driver to the database.
- **GET /driver/{driver_ref_name}:** Get details of a specific F1 driver.
- **PUT /driver/{driver_ref_name}:** Update details of a specific F1 driver.
- **DELETE /drivers/{driver_ref_name}:** Delete a specific F1 driver.
- **GET /results/{driver_id}:** Retrieve the race results of a F1 driver.
