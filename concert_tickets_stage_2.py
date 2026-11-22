# === Stage 2: Проверка полей ===
# Project: ConcertTickets
from datetime import datetime


def normalize_artist(artist: str) -> str:
    return artist.strip().title()


def normalize_venue(venue: str) -> str:
    return venue.strip().strip('.').title()


def normalize_date(date_str: str) -> str:
    for fmt in ('%d.%m.%Y', '%d.%m.%y', '%Y-%m-%d', '%Y.%m.%d'):
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime('%Y-%m-%d')
        except ValueError:
            continue
    raise ValueError('Дата в неправильном формате. Пример: 2025-12-31')


def normalize_price(price_str: str) -> float:
    cleaned = price_str.replace(',', '.').strip()
    try:
        return float(cleaned)
    except ValueError:
        raise ValueError('Цена должна быть числом')


def validate_artist(artist: str) -> str:
    if not artist or not artist.strip():
        raise ValueError('Артист не может быть пустым')
    return artist


def validate_venue(venue: str) -> str:
    if not venue or not venue.strip():
        raise ValueError('Площадка не может быть пустой')
    return venue


def validate_price(price) -> float:
    try:
        value = float(price)
    except (TypeError, ValueError):
        raise ValueError('Цена должна быть числом')
    if value <= 0:
        raise ValueError('Цена должна быть больше нуля')
    return value


def validate_date(date_str: str) -> str:
    try:
        return normalize_date(date_str)
    except ValueError:
        raise ValueError('Дата должна быть не раньше 01.01.1900')
    date = datetime.strptime(normalize_date(date_str), '%Y-%m-%d')
    if date.year < 1900:
        raise ValueError('Дата должна быть не раньше 01.01.1900')
    return date.strftime('%Y-%m-%d')


def validate_concert_fields(artist, venue, date_str, price) -> dict:
    try:
        return {
            'artist': validate_artist(artist),
            'venue': validate_venue(venue),
            'date': validate_date(date_str),
            'price': validate_price(price),
        }
    except ValueError as exc:
        raise ValueError(f'Ошибка данных билета: {exc}')
