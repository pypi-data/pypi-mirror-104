"""
Обучающая библиотека.

Создана для изучения программирования на примере создания простых двуxмерных игр.

Основные модули:
  world - управление игровым окном

  sprite - управление действующими объектами игры

  actions - то же, что и спрайт, но в режиме анимации

  sprite_text - работа с текстовыми спрайтами

  event_decorators - модуль для работы с событиями
"""

from wrap import w1 #wrap_py launcher
from wrap_mENdRU import world, const, sprite, actions, sprite_text, event_decorators
from wrap_mENdRU.event_decorators import * #import all event decotators in main module
from wrap_mENdRU.const import *

def add_sprite_dir(dir):
    """
    Добавляет папку в список мест, где будут искаться загружаемые спрайты.

    :param dir: Путь к папке со спрайтами. Например: C:\Temp
    """
    import wrap_data_source, wrap_py
    ds = wrap_data_source.file_data_source.FileDataSource(dir)
    wrap_py.site.sprite_data_sources.insert(0, ds)