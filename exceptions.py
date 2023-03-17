class NotForSending(Exception):
    """Не для пересылки в телеграм."""


class ProblemDescriptions(Exception):
    """Описания проблемы."""


class InvalidResponseCode(Exception):
    """Не верный код ответа."""


class ConnectinError(Exception):
    """Не верный код ответа."""


class EmptyResponseFromAPI(Exception):
    """Пустой ответ от API."""


class TelegramError(Exception):
    """Ошибка телеграма."""
