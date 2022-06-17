from app import db
from models import Pet

db.drop_all()
db.create_all()

