import logging
import os

from datetime import datetime

DEFAULT_PROJECT = "previsedx-quantstudio-file-utils"

DEFAULT_TIMESTAMP = str(datetime.today().strftime("%Y-%m-%d-%H%M%S"))

DEFAULT_OUTDIR_BASE = os.path.join(
    "/tmp/",
    os.getenv("USER"),
    DEFAULT_PROJECT,
)

DEFAULT_LOGGING_FORMAT = "%(levelname)s : %(asctime)s : %(pathname)s : %(lineno)d : %(message)s"

DEFAULT_LOGGING_LEVEL = logging.INFO

DEFAULT_VERBOSE = False

DEFAULT_CONFIG_FILE = os.path.join(
    os.path.dirname(__file__),
    "conf",
    "config.yaml"
)
