import logging
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

_audit_logs: List[Dict[str, Any]] = []

def record_audit(findings: List[Dict[str, Any]]):
    global _audit_logs
    _audit_logs = findings

def get_audit_logs():
    return _audit_logs
