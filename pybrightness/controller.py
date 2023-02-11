import os
import subprocess
from typing import NoReturn

from .module import settings


POWERSHELL = '(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,' + '{l}' + ')'


def eval_linux() -> NoReturn:
    """Evaluate root password for Linux.

    Raises:
        ValueError:
        If root_password is not set in Linux.
    """
    if not settings.root_password:
        raise ValueError(
            "'root_password' is required"
        )


def increase() -> NoReturn:
    """Increases the brightness to maximum."""
    if settings.operating_system == "Darwin":
        for _ in range(32):
            os.system("""osascript -e 'tell application "System Events"' -e 'key code 144' -e ' end tell'""")
    elif settings.operating_system == "Windows":
        subprocess.run(["powershell", POWERSHELL.format(l=100)])
    elif settings.operating_system == "Linux":
        eval_linux()
        os.system("echo %s | sudo -S brightnessctl s 100 > /dev/null" % settings.root_password)


def decrease() -> NoReturn:
    """Decreases the brightness to minimum."""
    if settings.operating_system == "Darwin":
        for _ in range(32):
            os.system("""osascript -e 'tell application "System Events"' -e 'key code 145' -e ' end tell'""")
    elif settings.operating_system == "Windows":
        subprocess.run(["powershell", POWERSHELL.format(l=0)])
    elif settings.operating_system == "Linux":
        eval_linux()
        os.system("echo %s | sudo -S brightnessctl s 0 > /dev/null" % settings.root_password)


def custom(percent: int = 50) -> NoReturn:
    """Set brightness to a custom level.

    - | Since package uses in-built apple script (for macOS), the only way to achieve this is to set the
      | brightness to absolute minimum/maximum and increase/decrease the required % from there.

    Args:
        percent: Percentage of brightness to be set.
    """
    if settings.operating_system == "Darwin":
        decrease()
        for _ in range(round((32 * int(percent)) / 100)):
            os.system("""osascript -e 'tell application "System Events"' -e 'key code 144' -e ' end tell'""")
    elif settings.operating_system == "Windows":
        subprocess.run(["powershell", POWERSHELL.format(l=percent)])
    elif settings.operating_system == "Linux":
        eval_linux()
        os.system("echo %s | sudo -S brightnessctl s %d > /dev/null" % (settings.root_password, percent))
