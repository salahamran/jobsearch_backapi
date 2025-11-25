"""Resume info and the attachments."""

from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from app.core.database import Base
from sqlalchemy.orm import relationship


class Resume(Base):
    """The raw data whcih was collected from users, files and etc."""

    __tablename__ = 'resumes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    resume_text = Column(Text)
    resume_file_url = Column(String)
    last_updated = Column(DateTime)

    user = relationship('User', back_populates='resumes')
