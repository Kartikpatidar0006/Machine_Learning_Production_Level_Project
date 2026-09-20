import logging
import os
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H-%M-%S')}.log"
log_dir = PROJECT_ROOT / "logs"
log_dir.mkdir(parents=True, exist_ok=True)
logs_path = log_dir / LOG_FILE

logging.basicConfig(
    filename=str(logs_path),
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)