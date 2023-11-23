"""Parent module for settings wrapper."""

import logging
import platform
from typing import AnyStr, Union


def _get_root_pass() -> Union[str, None]:
    """Get root password from environment variables for Linux machines."""
    import os
    import dotenv
    dotenv.load_dotenv(dotenv_path=os.environ.get("env_file", os.environ.get("ENV_FILE", ".env")))
    rp = os.environ.get('ROOT_PASSWORD') or os.environ.get('root_password')
    return rp


class Settings:
    """Wrapper for settings.

    >>> Settings

    """

    operating_system: str = platform.system()
    if operating_system not in ("Linux", "Darwin", "Windows"):
        raise OSError(
            "Package is unsupported in %s" % operating_system
        )
    if operating_system == "Linux":
        root_password: AnyStr = _get_root_pass()
    logger: logging.Logger = None


settings = Settings()


class Commands:
    """Unique commands for macOS and Windows.

    >>> Commands

    """

    MAC_DECREASE = """osascript -e 'tell application "System Events"' -e 'key code 145' -e ' end tell'"""
    MAC_INCREASE = """osascript -e 'tell application "System Events"' -e 'key code 144' -e ' end tell'"""
    WINDOWS = '(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,' + '{l}' + ')'


commands = Commands()
