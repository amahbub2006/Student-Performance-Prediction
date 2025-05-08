import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_PATH = os.path.join(LOG_DIR, LOG_FILE)
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s",
)

logger = logging.getLogger("studentml_logger")
