import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", 17584090))
      API_HASH = os.environ.get("3f779654fdd3b9278fd95869aabf4593")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "DeoxysX")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 7252430326 )) 
      DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Aaki8490:vnCMn6F5l8nqXxFe@cluster0.jlgdebe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
