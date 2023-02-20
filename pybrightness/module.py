import os
import platform
from typing import AnyStr

import dotenv

dotenv.load_dotenv(dotenv_path=".env")


class Settings:
    """Wrapper for settings.

    >>> Settings

    """

    operating_system = str(platform.system())
    root_password: AnyStr = os.environ.get('ROOT_PASSWORD') or os.environ.get('root_password')
    if operating_system not in ("Linux", "Darwin", "Windows"):
        raise OSError(
            "Package is unsupported in %s" % operating_system
        )


settings = Settings()
