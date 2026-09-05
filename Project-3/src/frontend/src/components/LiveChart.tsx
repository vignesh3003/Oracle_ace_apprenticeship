"use client";

import React from "react";
import { Activity } from "lucide-react";

interface LiveChartProps {
  metrics: any[];
}

export const LiveChart: React.FC<LiveChartProps> = ({ metrics }) => {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-base font-bold text-white flex items-center gap-2">
          <Activity className="w-5 h-5 text-sky-400" />
          Real-Time OCI Ampere CPU & RAM Telemetry Stream
        </h2>
        <span className="text-xs text-slate-400 font-mono">Sampled via daemon daemon every 5s</span>
      </div>

      <div className="space-y-3">
        {metrics.slice(0, 5).map((m, idx) => (
          <div key={idx} className="bg-slate-850 p-3 rounded-lg border border-slate-800 space-y-1.5 font-mono text-xs">
            <div className="flex justify-between text-slate-300">
              <span>{m.host_name || "oci-ampere-arm-vm-01"}</span>
              <span className="text-slate-500">{m.recorded_at}</span>
            </div>
            <div className="w-full bg-slate-800 rounded-full h-2 overflow-hidden flex">
              <div className="bg-sky-500 h-2" style={{ width: `${m.cpu_utilization_pct}%` }}></div>
            </div>
            <div className="flex justify-between text-[11px] text-slate-400">
              <span>CPU: {m.cpu_utilization_pct}%</span>
              <span>RAM: {m.memory_utilization_pct}%</span>
              <span>Net RX: {m.network_rx_kbps} KB/s</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
