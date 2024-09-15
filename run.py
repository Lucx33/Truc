from app import create_app
import pandas as pd

# Cria o app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
