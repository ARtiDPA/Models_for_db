"""Простая модель для авторизации"""
from sqlalchemy import Integer, String, MetaData
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    metadata = MetaData('shemas_name')


class User(Base):
    """Модель бд для пользователя

    Args:
        Base (class): Base class
    """

    __tablename__ = 'user'
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String(256))
    access_level: Mapped[Integer] = mapped_column(Integer, default=0)
