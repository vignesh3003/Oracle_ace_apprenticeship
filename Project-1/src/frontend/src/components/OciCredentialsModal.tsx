"use client";

import React from "react";
import { X, Key, Database, Cloud, ShieldCheck } from "lucide-react";

interface OciCredentialsModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export const OciCredentialsModal: React.FC<OciCredentialsModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl max-w-2xl w-full max-h-[90vh] overflow-y-auto p-6 shadow-2xl border border-gray-200 text-oracle-dark">
        <div className="flex items-center justify-between border-b pb-4 mb-4">
          <div className="flex items-center space-x-2">
            <Key className="w-5 h-5 text-oracle-red" />
            <h2 className="text-lg font-bold">Real OCI Cloud Connection Guide</h2>
          </div>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-600">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="space-y-4 text-xs leading-relaxed text-gray-700">
          <div className="bg-blue-50 border border-blue-200 p-3 rounded-lg flex items-start gap-2">
            <ShieldCheck className="w-5 h-5 text-blue-600 shrink-0 mt-0.5" />
            <p>
              By default, OracleDocuAI runs in <strong>Local Demo Simulation Mode</strong> out-of-the-box so you can inspect UI and vector search features without active cloud credentials. Follow the steps below when connecting your live OCI account.
            </p>
          </div>

          <div className="space-y-2">
            <h3 className="font-bold text-sm text-oracle-red flex items-center gap-1">
              <Cloud className="w-4 h-4" /> 1. OCI API Key & Config (~/.oci/config)
            </h3>
            <p>In OCI Console $\rightarrow$ Profile $\rightarrow$ User Settings $\rightarrow$ API Keys $\rightarrow$ Add API Key. Download key and paste into `~/.oci/config`:</p>
            <pre className="bg-oracle-dark text-emerald-400 p-3 rounded font-mono text-[11px] overflow-x-auto">
{`[DEFAULT]
user=ocid1.user.oc1..aaaaaaaaxxx
fingerprint=xx:xx:xx:xx:xx:xx
tenancy=ocid1.tenancy.oc1..aaaaaaaaxxx
region=us-ashburn-1
key_file=~/.oci/oci_api_key.pem`}
            </pre>
          </div>

          <div className="space-y-2">
            <h3 className="font-bold text-sm text-oracle-red flex items-center gap-1">
              <Database className="w-4 h-4" /> 2. Oracle Autonomous Database 23ai DSN & Wallet
            </h3>
            <p>In OCI Console $\rightarrow$ Oracle Autonomous Database Details $\rightarrow$ DB Connection $\rightarrow$ Download Wallet. Place contents in `oracle_wallet/` and update backend `.env`:</p>
            <pre className="bg-oracle-dark text-emerald-400 p-3 rounded font-mono text-[11px] overflow-x-auto">
{`APP_ENV=production
OCI_COMPARTMENT_ID=ocid1.compartment.oc1..aaaaaaaaxxx
ORACLE_DB_USER=admin
ORACLE_DB_PASSWORD=YourStrongPassword23ai!
ORACLE_DB_DSN=docuai23db_high
ORACLE_DB_WALLET_LOCATION=/app/oracle_wallet`}
            </pre>
          </div>
        </div>

        <div className="mt-6 flex justify-end">
          <button
            onClick={onClose}
            className="bg-oracle-red text-white text-xs font-semibold px-4 py-2 rounded-lg hover:bg-red-700 transition-colors"
          >
            Got it, Close Guide
          </button>
        </div>
      </div>
    </div>
  );
};
