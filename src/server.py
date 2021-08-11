from app import app
import os
import controllers.root_controller
import controllers.fetch

app.run("0.0.0.0", os.getenv("PORT"), debug=True)