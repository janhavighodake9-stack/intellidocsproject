from services.document_services import get_welcome_message


def home():
    return get_welcome_message()