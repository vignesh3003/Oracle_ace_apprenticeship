"use client";

import React from "react";
import { ShieldCheck, Lock, Database } from "lucide-react";

export const Header: React.FC = () => {
  return (
    <header className="bg-slate-900 border-b border-slate-800 py-4 px-6 sticky top-0 z-40">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="bg-emerald-600 p-2 rounded-lg text-white">
            <ShieldCheck className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-white flex items-center gap-2">
              OracleCloudGuard-X
              <span className="bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 text-xs px-2 py-0.5 rounded-full font-mono">
                OCI Vault KMS
              </span>
            </h1>
            <p className="text-xs text-slate-400">
              OCI Vault Key Management $\rightarrow$ OCI ONS Notifications $\rightarrow$ Oracle DB Audit Log
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-3 text-xs bg-slate-800/80 px-3 py-1.5 rounded-md border border-slate-700 font-mono">
          <Lock className="w-4 h-4 text-emerald-400" />
          <span>AES-256 Secrets</span>
          <span className="text-slate-600">•</span>
          <Database className="w-4 h-4 text-sky-400" />
          <span>Autonomous DB</span>
        </div>
      </div>
    </header>
  );
};
