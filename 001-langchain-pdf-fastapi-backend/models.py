from sqlalchemy import Boolean, Column, LargeBinary, Integer, Text
from database import Base

class PDF(Base):
    __tablename__ = "pdfs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text)
    file = Column(Text)
    selected = Column(Boolean, default=False)