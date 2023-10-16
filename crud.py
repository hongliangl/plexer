from sqlalchemy.orm import Session
import models


def get_source(db: Session, uid: str):
    return db.query(models.Source).filter(models.Source.uid == uid).first()


def get_destination(db: Session, uid: str):
    return db.query(models.Destination).filter(models.Destination.uid == uid).first()
