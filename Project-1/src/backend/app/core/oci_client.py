import logging
from typing import Optional, Tuple
from app.config import settings

logger = logging.getLogger(__name__)

# Global client placeholders
_oci_config = None
_object_storage_client = None
_vision_client = None

def get_oci_config():
    """Load OCI SDK Config from standard config file (~/.oci/config) or API keys."""
    global _oci_config
    if settings.is_demo_mode:
        logger.info("[OCI SDK] Running in Demo/Development Mode. Bypassing ~/.oci/config authentication.")
        return None

    if _oci_config is None:
        try:
            import oci
            _oci_config = oci.config.from_file(
                file_location=settings.OCI_CONFIG_FILE,
                profile_name=settings.OCI_PROFILE
            )
            logger.info(f"[OCI SDK] Successfully authenticated OCI Config profile: {settings.OCI_PROFILE}")
        except Exception as e:
            logger.warning(f"[OCI SDK] Could not load OCI config from {settings.OCI_CONFIG_FILE}: {e}")
            logger.info("[OCI SDK] Falling back to Demo Mode.")
            return None
    return _oci_config

def get_object_storage_client():
    """Initialize official OCI ObjectStorageClient using Python OCI SDK."""
    global _object_storage_client
    config = get_oci_config()
    if config is None:
        return None

    if _object_storage_client is None:
        try:
            import oci
            _object_storage_client = oci.object_storage.ObjectStorageClient(config)
            logger.info("[OCI Object Storage] Client initialized successfully.")
        except Exception as e:
            logger.error(f"[OCI Object Storage] Failed to initialize client: {e}")
            return None
    return _object_storage_client

def get_vision_client():
    """Initialize official OCI AIServiceVisionClient using Python OCI SDK."""
    global _vision_client
    config = get_oci_config()
    if config is None:
        return None

    if _vision_client is None:
        try:
            import oci
            kwargs = {}
            if settings.OCI_VISION_ENDPOINT:
                kwargs["service_endpoint"] = settings.OCI_VISION_ENDPOINT
            _vision_client = oci.ai_vision.AIServiceVisionClient(config, **kwargs)
            logger.info("[OCI Vision AI] Client initialized successfully.")
        except Exception as e:
            logger.error(f"[OCI Vision AI] Failed to initialize client: {e}")
            return None
    return _vision_client
