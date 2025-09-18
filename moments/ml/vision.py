# moments/ml/vision.py
import os, requests, json
from typing import Tuple, List

def caption_and_tags(image_bytes: bytes) -> Tuple[str, List[str]]:
    """
    Returns (caption, tags) for an image using Azure Vision API.
    Expects AZURE_VISION_ENDPOINT and AZURE_VISION_KEY in env.
    """
    print('helooooooooooeoeoeoeoeooeoeoeoeoeoeoeooeoeoeoeeoeoe')
    endpoint = os.environ.get("AZURE_VISION_ENDPOINT", "").rstrip("/")
    key = os.environ.get("AZURE_VISION_KEY")
    if not endpoint or not key:
        raise RuntimeError("Azure Vision credentials not set.")

    # Use the updated API version
    url = f"{endpoint}/computervision/imageanalysis:analyze"
    params = {"api-version": "2023-10-01", "features": "caption,tags"}  # updated here
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/octet-stream"
    }

    resp = requests.post(url, params=params, headers=headers, data=image_bytes, timeout=20)
    print(resp)
    resp.raise_for_status()
    data = resp.json()
    print(data)
    # The response structure is the same
    caption = (data.get("captionResult") or {}).get("text") or ""
    tags = [t["name"] for t in data.get("tagsResult", {}).get("values", []) if "name" in t]
    return caption, tags
