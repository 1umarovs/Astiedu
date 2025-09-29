from django.utils.translation import get_language
from .utils import get_text

def translations(request):
    lang = (get_language() or "en").split("-")[0]
    return {"t": get_text(lang)}
