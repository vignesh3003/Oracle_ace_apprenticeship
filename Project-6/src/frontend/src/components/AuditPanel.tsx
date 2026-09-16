"use client";

import React, { useState } from "react";
import { ShieldAlert, Play, CheckCircle2, Loader2 } from "lucide-react";

export const AuditPanel: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [findings, setFindings] = useState<any[]>([
    {
      rule_id: "SEC-001",
      resource: "OCI Vault Secret Management",
      status: "COMPLIANT",
      details: "All database passwords and API keys stored securely inside encrypted OCI Vault secrets."
    },
    {
      rule_id: "SEC-002",
      resource: "OCI Compartment IAM Policies",
      status: "COMPLIANT",
      details: "Least privilege policy configured. Anonymous public write access disabled."
    }
  ]);

  const handleScan = async () => {
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/api/v1/audit/run", { method: "POST" });
      const data = await res.json();
      setFindings(data.findings || []);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 space-y-6 shadow-xl">
      <div className="flex items-center justify-between">
        <h2 className="text-base font-bold text-white flex items-center gap-2">
          <ShieldAlert className="w-5 h-5 text-emerald-400" />
          Automated OCI Security & Vault Compliance Auditor
        </h2>
        <button
          onClick={handleScan}
          disabled={loading}
          className="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-2 transition-colors disabled:opacity-50"
        >
          {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Play className="w-4 h-4" />}
          Trigger Security Audit Scan
        </button>
      </div>

      <div className="space-y-3">
        {findings.map((f, idx) => (
          <div key={idx} className="bg-slate-850 border border-slate-800 p-4 rounded-lg space-y-1 text-xs">
            <div className="flex items-center justify-between">
              <span className="font-bold text-slate-200 font-mono">[{f.rule_id}] {f.resource}</span>
              <span className="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 px-2 py-0.5 rounded text-[10px] font-mono flex items-center gap-1">
                <CheckCircle2 className="w-3 h-3" />
                {f.status}
              </span>
            </div>
            <p className="text-slate-400 leading-relaxed">{f.details}</p>
          </div>
        ))}
      </div>
    </div>
  );
};
