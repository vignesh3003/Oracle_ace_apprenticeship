"use client";

import React from "react";
import { Cpu, Bell, Server, Database } from "lucide-react";

export const Header: React.FC = () => {
  return (
    <header className="bg-slate-900 border-b border-slate-800 py-4 px-6 sticky top-0 z-40">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="bg-red-600 p-2 rounded-lg text-white">
            <Cpu className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-white flex items-center gap-2">
              OracleTelemetryX
              <span className="bg-emerald-500/20 text-emerald-400 border border-emerald-500/40 text-xs px-2 py-0.5 rounded-full font-mono">
                OCI Ampere ARM VM
              </span>
            </h1>
            <p className="text-xs text-slate-400">
              OCI Compute ARM64 $\rightarrow$ python-oracledb SessionPool $\rightarrow$ OCI ONS Notification Engine
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-3 text-xs bg-slate-800/80 px-3 py-1.5 rounded-md border border-slate-700 font-mono">
          <Server className="w-4 h-4 text-sky-400" />
          <span>Ampere A1 Flex</span>
          <span className="text-slate-600">•</span>
          <Bell className="w-4 h-4 text-amber-400" />
          <span>OCI ONS Topics</span>
        </div>
      </div>
    </header>
  );
};
