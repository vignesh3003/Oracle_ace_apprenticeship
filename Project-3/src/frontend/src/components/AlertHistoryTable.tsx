"use client";

import React from "react";
import { AlertTriangle, BellCheck } from "lucide-react";

interface AlertHistoryTableProps {
  anomalies: any[];
}

export const AlertHistoryTable: React.FC<AlertHistoryTableProps> = ({ anomalies }) => {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-base font-bold text-white flex items-center gap-2">
          <AlertTriangle className="w-5 h-5 text-amber-400" />
          Z-Score Anomaly Alerts & OCI ONS Notification Audit Log
        </h2>
        <span className="text-xs text-slate-400 font-mono">Oracle ADB Telemetry Table</span>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs font-mono">
          <thead className="bg-slate-800 text-slate-400 uppercase text-[10px]">
            <tr>
              <th className="p-2.5">Alert ID</th>
              <th className="p-2.5">Host</th>
              <th className="p-2.5">Metric</th>
              <th className="p-2.5">Observed</th>
              <th className="p-2.5">Z-Score</th>
              <th className="p-2.5">ONS Status</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800 text-slate-300">
            {anomalies.length === 0 ? (
              <tr>
                <td colSpan={6} className="p-4 text-center text-slate-500">No anomaly alerts triggered. All host metrics normal.</td>
              </tr>
            ) : (
              anomalies.map((a) => (
                <tr key={a.alert_id} className="hover:bg-slate-800/50">
                  <td className="p-2.5 text-red-400 font-bold">#{a.alert_id}</td>
                  <td className="p-2.5">{a.host_name}</td>
                  <td className="p-2.5">{a.metric_type}</td>
                  <td className="p-2.5 text-amber-300">{a.observed_value}%</td>
                  <td className="p-2.5">{a.z_score}</td>
                  <td className="p-2.5 flex items-center gap-1 text-emerald-400">
                    <BellCheck className="w-3.5 h-3.5" />
                    {a.ons_notification_status}
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};
