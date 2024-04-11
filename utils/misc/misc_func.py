from typing import Dict
from telebot.types import InputMediaPhoto


def insert_img(img: str, caption: Dict) -> InputMediaPhoto(str, str):
    """Функция для формирования фото с описанием, для передачи"""
    return InputMediaPhoto(img, f'Название: {caption["name"]}'
                                f'\nЦена за ночь: {caption["price"]}'
                                f'\nРасстояние до центра: {caption["distance_from_center"]}'
                                f'\nЦена за выбранный период: {caption["total_price"]}$'
                                f'\nСайт: {caption["urls"]}')
