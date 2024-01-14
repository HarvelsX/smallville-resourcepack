import tomllib

from pathlib import Path

PACK_CONFIG_PATH = Path("pack.toml")


def get_pack_config() -> dict:
    return tomllib.loads(PACK_CONFIG_PATH.read_text())
