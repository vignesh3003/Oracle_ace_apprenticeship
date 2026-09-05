import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Serverless Feedback Pulse API"
    APP_ENV: str = "development"
    PORT: int = 8000
    ORACLE_SODA_URL: str = "https://docuai23db.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/soda/latest/feedback_collection"
    ORACLE_DB_USER: str = "admin"
    ORACLE_DB_PASSWORD: str = "YourStrongPassword23ai!"
    OCI_CONFIG_FILE: str = os.path.expanduser("~/.oci/config")
    OCI_COMPARTMENT_ID: str = "ocid1.compartment.oc1..example"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
