from fileParser import load_parsed_data
import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker

engine = sa.create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class DataRecord(Base):
    __tablename__ = 'data_records'
    lap = sa.Column(sa.Integer, primary_key=True)
    time = sa.Column(sa.Float)

with Session() as session:
    Base.metadata.create_all(engine)
    parsed_data = load_parsed_data()
    for idx, lap in enumerate(parsed_data["lap_data"]):
        lap_time_str = lap["lap_time"]
        #minutes, seconds = lap_time_str.split(':')
        #total_seconds = int(minutes) * 60 + float(seconds)
        record = DataRecord(lap=idx, time=lap_time_str)
        session.add(record)
        print(record)
    #session.commit()


