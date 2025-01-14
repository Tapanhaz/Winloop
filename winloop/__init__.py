import asyncio as __asyncio
import typing as _typing

from asyncio.events import BaseDefaultEventLoopPolicy as __BasePolicy

# from . import includes as __includes  # NOQA
from .loop import Loop as __BaseLoop  # NOQA
# from ._version import __version__  # NOQA


__all__ = ('new_event_loop', 'install', 'WinLoopPolicy')


class Loop(__BaseLoop, __asyncio.AbstractEventLoop):  # type: ignore[misc]
    pass


def new_event_loop() -> Loop:
    """Returns a new event loop."""
    return Loop()


def install() -> None:
    """A helper function to install winloop policy."""
    __asyncio.set_event_loop_policy(WinLoopPolicy())


class WinLoopPolicy(__BasePolicy):
    """Event loop policy.
    The preferred way to make your application use winloop:
    >>> import asyncio
    >>> import winloop
    >>> asyncio.set_event_loop_policy(winloop.WinLoopPolicy())
    >>> asyncio.get_event_loop()
    "<winloop.Loop running=False closed=False debug=False>"
    """

    def _loop_factory(self) -> Loop:
        return new_event_loop()

    if _typing.TYPE_CHECKING:
        # EventLoopPolicy doesn't implement these, but since they are marked
        # as abstract in typeshed, we have to put them in so mypy thinks
        # the base methods are overridden. This is the same approach taken
        # for the Windows event loop policy classes in typeshed.
        def get_child_watcher(self) -> _typing.NoReturn:
            ...

        def set_child_watcher(
            self, watcher: _typing.Any
        ) -> _typing.NoReturn:
            ...
