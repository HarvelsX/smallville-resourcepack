import requests

VERSIONS_MANIFEST = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"


def get_version(version: str) -> dict:
    response = requests.get(VERSIONS_MANIFEST).json()
    if "versions" not in response:
        return {}

    manifest_versions = response["versions"]
    manifest_version = next(
        (i for i in manifest_versions if "id" in i and i["id"] == version), {}
    )
    if "url" not in manifest_version:
        return {}

    url = manifest_version["url"]
    return requests.get(url).json()


def get_asset_index(version: str) -> dict:
    version_manifest = get_version(version)
    if "assetIndex" not in version_manifest:
        return {}

    manifest_version_asset_index = version_manifest["assetIndex"]
    if "url" not in manifest_version_asset_index:
        return {}

    url = manifest_version_asset_index["url"]
    return requests.get(url).json()
