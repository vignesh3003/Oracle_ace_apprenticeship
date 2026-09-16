import logging
from fastapi import APIRouter
from app.core.oci_vault import audit_security_compliance
from app.db.connection import record_audit

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/audit", tags=["OCI Security Audit"])

@router.post("/run")
def trigger_compliance_scan():
    findings = audit_security_compliance()
    record_audit(findings)
    return {
        "status": "scan_completed",
        "total_rules_checked": len(findings),
        "findings": findings,
        "oracle_services": ["OCI Vault (KMS)", "OCI Notification Service (ONS)", "Oracle Autonomous DB"]
    }

@router.get("/report")
def get_report():
    findings = audit_security_compliance()
    return {"status": "success", "findings": findings}
