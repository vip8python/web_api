from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = 'profile'

    firstname: Mapped[str | None] = mapped_column(String(40))
    lastname: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]
