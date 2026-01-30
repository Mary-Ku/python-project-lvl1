"""Модуль содержит описание типов приложения brain games."""

from collections.abc import Callable

GetMainDataFunc = Callable[..., tuple[str, str]]

RunGameFunc = Callable[..., tuple[str, GetMainDataFunc]]
