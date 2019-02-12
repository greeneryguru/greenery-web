from passlib.hash import pbkdf2_sha256
from sqlalchemy import (Column, Integer, String, Text, Boolean, Float,
        DateTime, ForeignKey, func)
from potnanny.core.database import Base, db_session


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(48))
    password = Column(String(256))
    is_active = Column(Boolean, default=True)
    created = Column(DateTime, default=func.now())

    def __repr__(self):
        return "<User({})>".format(self.username)

    def set_password(self, pw):
        self.password = pbkdf2_sha256.hash(pw, rounds=200000, salt_size=16)
        db_session.commit()

    def check_password(self, pw):
        return pbkdf2_sha256.verify(pw, self.password)
