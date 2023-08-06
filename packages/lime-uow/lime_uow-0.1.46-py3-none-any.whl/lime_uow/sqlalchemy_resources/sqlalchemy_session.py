from __future__ import annotations

import typing

from sqlalchemy import orm

from lime_uow import exceptions, resource

__all__ = ("SqlAlchemySession",)


class SqlAlchemySession(resource.Resource[orm.Session]):
    def __init__(self, session_factory: orm.sessionmaker, /):
        self._session_factory = session_factory
        self._session: typing.Optional[orm.Session] = None

    @staticmethod
    def key() -> str:
        return SqlAlchemySession.__name__

    def open(self, **kwargs: typing.Dict[str, typing.Any]) -> orm.Session:
        self._session = self._session_factory()
        return self._session

    def close(self) -> None:
        if self._session:
            self._session.close()
            self._session = None

    def rollback(self) -> None:
        if self._session is None:
            raise exceptions.RollbackError(
                "Attempted to rollback a closed session.",
            )
        else:
            self._session.rollback()

    def save(self) -> None:
        if self._session:
            self._session.commit()
