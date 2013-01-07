from catalog.clock_features import *

def clock_features(request):
    return {
        'mechanisms': MECHANISM_CHOICES,
        }