import os
import dotenv

dotenv.load_dotenv()

ATLAS = os.getenv("ATLAS")

mongo_url = f"mongodb+srv://{ATLAS}@cluster0.qlsum.mongodb.net/bcn_data?retryWrites=true&w=majority"