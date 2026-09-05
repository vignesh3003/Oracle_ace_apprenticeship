import logging
from app.config import settings

logger = logging.getLogger(__name__)

def publish_ons_alert(subject: str, message_body: str) -> bool:
    """Publish real-time anomaly notification to OCI Notification Service (ONS) Topic via OCI SDK."""
    if settings.is_demo_mode or not settings.OCI_ONS_TOPIC_OCID:
        logger.info(f"[OCI ONS Simulation] Alert Subject: '{subject}' $\rightarrow$ ONS Email Alert Simulated.")
        return True

    try:
        import oci
        config = oci.config.from_file(
            file_location=settings.OCI_CONFIG_FILE,
            profile_name=settings.OCI_PROFILE
        )
        ons_client = oci.ons.NotificationDataPlaneClient(config)
        message_details = oci.ons.models.MessageDetails(
            title=subject,
            body=message_body
        )
        res = ons_client.publish_message(
            topic_id=settings.OCI_ONS_TOPIC_OCID,
            message_details=message_details
        )
        logger.info(f"[OCI ONS SDK Success] Message ID: {res.data.message_id}")
        return True
    except Exception as e:
        logger.error(f"[OCI ONS API Error] {e}")
        return False
