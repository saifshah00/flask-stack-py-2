import os
from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(db_connection_string)

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"), {"val": id}
        )
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0]._mapping)
