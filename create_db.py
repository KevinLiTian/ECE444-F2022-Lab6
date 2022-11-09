# create_db.py


from project.app import app, db


# create the database and the db table
with app.app_context():
    db.create_all()

    # commit the changes
    db.session.commit()
