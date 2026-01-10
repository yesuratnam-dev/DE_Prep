# utils/fda_utils.py
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

MANIFEST_URL = "https://api.fda.gov/download.json"

def get_fda_manifest_node(product: str, endpoint: str, timeout=60):
    """
    Returns the manifest node for a specific product & endpoint.

    Example usage:
        node = get_fda_manifest_node("drug", "shortages")
    """
    # Configure session with retry strategy
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    # Get manifest
    resp = session.get(MANIFEST_URL, timeout=timeout, verify=True)
    resp.raise_for_status()
    manifest = resp.json()

    node = manifest["results"][product][endpoint]
    return node , session
