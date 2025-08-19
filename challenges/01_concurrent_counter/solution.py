import time

DELAY_SECONDS = 0.002

class Counter:
    """Non thread-safe counter (starter implementation)."""
    def __init__(self):
        self.count = 0

    def increment(self):
        current = self.count
        time.sleep(DELAY_SECONDS)
        self.count = current + 1

# --- START YOUR SOLUTION HERE ---
import threading

# se crea un lock global para sincronizar las llamadas y se referencia al método original de la calse
_counter_lock = threading.Lock()

_original_increment = Counter.increment

def _safe_increment(self):
    # Se define una nueva versión segura del método increment
    with _counter_lock:
        return _original_increment(self)

# Reemplazamos el método original por el thread-safe
Counter.increment = _safe_increment

# --- END OF YOUR SOLUTION ---
