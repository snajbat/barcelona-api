from app import app
from config import PORT
import controllers.root_controller
import controllers.fetch

app.run("0.0.0.0", PORT, debug=True)