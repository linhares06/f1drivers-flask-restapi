import config

# Initialize the Connexion application using the ConnexionApp instance from the 'config' module.
app = config.connex_app

# Add the API specification from the Swagger YAML file to the Connexion application.
app.add_api(config.basedir / "swagger.yml")

# Entry point of the script: if this script is executed directly (not imported), run the application.
if __name__ == "__main__":
    # Enable debugging mode for the Connexion application.
    app.debug = True
    
    # Run the Connexion application on the specified host and port.
    app.run(host="0.0.0.0", port=8000)