
from django.conf import settings
from random import choice
from string import ascii_letters, digits
keySize = getattr(settings, "MAXIMUM_URL_CHARS", 8)
avail = ascii_letters + digits


def create_random_code(chars=avail):
    return "".join(
        [choice(chars) for _ in range(keySize)])
        
def create_shortened_url(model_instance):
    random_code = create_random_code()
    model_class = model_instance.__class__

    if model_class.objects.filter(newURL=random_code).exists():
        return create_shortened_url(model_instance)
    return random_code