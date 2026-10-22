"""Entry point for Pomodoro Focus."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common_app import launch

if __name__ == "__main__":
    raise SystemExit(launch("06_pomodoro_focus"))
