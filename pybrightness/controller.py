"""Parent module to control brightness."""

import logging
import subprocess
from typing import Union, List

from .module import settings, commands

OS_ERROR = OSError("Package is unsupported in %s" % settings.operating_system)


def eval_linux() -> None:
    """Evaluate root password for Linux.

    Raises:
        ValueError:
        If root_password is not set in Linux.
    """
    if not settings.root_password:
        raise ValueError(
            "'root_password' is required"
        )


def _run(cmd: Union[str, List[str]]) -> None:
    """Runs the command using subprocess module.

    Args:
        cmd: Command to run.
    """
    result = subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode and settings.logger:
        settings.logger.error("Command `%s` failed with error code: %d", result.args, result.returncode)


def increase(logger: logging.Logger = None) -> None:
    """Increases the brightness to maximum."""
    settings.logger = logger
    if settings.operating_system == "Darwin":
        for _ in range(16):
            _run(commands.MAC_INCREASE)
    elif settings.operating_system == "Windows":
        _run(["powershell", commands.WINDOWS.format(l=100)])
    elif settings.operating_system == "Linux":
        eval_linux()
        _run(f"echo {settings.root_password} | sudo -S brightnessctl s 100 > /dev/null")
    else:
        raise OS_ERROR


def decrease(logger: logging.Logger = None) -> None:
    """Decreases the brightness to minimum."""
    settings.logger = logger
    if settings.operating_system == "Darwin":
        for _ in range(16):
            _run(commands.MAC_DECREASE)
    elif settings.operating_system == "Windows":
        _run(["powershell", commands.WINDOWS.format(l=0)])
    elif settings.operating_system == "Linux":
        eval_linux()
        _run(f"echo {settings.root_password} | sudo -S brightnessctl s 0 > /dev/null")
    else:
        raise OS_ERROR


def custom(percent: int, logger: logging.Logger = None) -> None:
    """Set brightness to a custom level.

    - | Since package uses in-built apple script (for macOS), the only way to achieve this is to set the
      | brightness to absolute minimum/maximum and increase/decrease the required % from there.

    Args:
        percent: Percentage of brightness to be set.
        logger: Bring your own logger.
    """
    settings.logger = logger
    assert isinstance(percent, int) and 0 <= percent <= 100, "value should be an integer between 0 and 100"
    if settings.operating_system == "Darwin":
        decrease()
        for _ in range(round((16 * int(percent)) / 100)):
            _run(commands.MAC_INCREASE)
    elif settings.operating_system == "Windows":
        _run(["powershell", commands.WINDOWS.format(l=percent)])
    elif settings.operating_system == "Linux":
        eval_linux()
        _run(f"echo {settings.root_password} | sudo -S brightnessctl s {percent} > /dev/null")
    else:
        raise OS_ERROR
