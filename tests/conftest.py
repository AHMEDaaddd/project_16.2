"""Настройка путей для корректного импорта src в тестах."""

import os
import sys

# Добавляет src/ в sys.path для корректного импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
