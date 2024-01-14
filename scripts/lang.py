#!/usr/bin/env python3
import shutil

from pathlib import Path

from resources import get_asset_index
from configs import get_pack_config

BASE_LANG = "en_us"


def main():
    pack_config = get_pack_config()
    minecraft_version = pack_config["minecraft_version"]

    asset_index = get_asset_index(minecraft_version)
    asset_objects: dict = asset_index["objects"]

    langs: list[str] = [
        key[len("minecraft/lang/") : -len(".json")]
        for key in asset_objects.keys()
        if key.startswith("minecraft/lang/")
    ]

    print(langs)

    langs_path = Path(f"src/assets/minecraft/lang")
    base_lang_path = langs_path / f"{BASE_LANG}.json"

    for lang in langs:
        shutil.copy(base_lang_path, langs_path / f"{lang}.json")


if __name__ == "__main__":
    main()
