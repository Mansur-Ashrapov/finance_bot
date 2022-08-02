from app.database import db, models

models.Base.metadata.create_all(bind=db.engine)

