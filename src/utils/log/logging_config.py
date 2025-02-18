import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("src/utils/log/weather_app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)