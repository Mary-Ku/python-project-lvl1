"""Модуль содержит описание типов приложения brain games."""

from collections.abc import Callable

GetMainDataFunc = Callable[..., tuple[str | int, str]]

RunGameFunc = Callable[..., tuple[str, GetMainDataFunc]]
