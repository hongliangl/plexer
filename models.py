from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Source(Base):
    __tablename__ = "sources"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)


class Destination(Base):
    __tablename__ = "destinations"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
