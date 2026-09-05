#!/usr/bin/env bash
# =============================================================================
# Oracle Autonomous JSON Database: SODA Collection Initializer
# Creates the SODA JSON Document Collection via Oracle REST Data Services (ORDS)
# =============================================================================

SODA_BASE_URL="https://docuai23db.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/soda/latest"
DB_USER="admin"
DB_PASS="YourStrongPassword23ai!"
COLLECTION_NAME="feedback_collection"

echo "Creating SODA Collection '${COLLECTION_NAME}' in Oracle Autonomous JSON Database..."

curl -X PUT "${SODA_BASE_URL}/${COLLECTION_NAME}" \
     -u "${DB_USER}:${DB_PASS}" \
     -H "Content-Type: application/json"

echo -e "\nVerifying SODA Collections list:"
curl -X GET "${SODA_BASE_URL}" \
     -u "${DB_USER}:${DB_PASS}"

echo -e "\nSODA Bootstrap Complete!"
