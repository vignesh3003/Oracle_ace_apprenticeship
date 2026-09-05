"use client";

import React from "react";

interface MetricCardProps {
  title: string;
  value: string;
  subtitle: string;
  icon: React.ReactNode;
  alert?: boolean;
}

export const MetricCard: React.FC<MetricCardProps> = ({ title, value, subtitle, icon, alert }) => {
  return (
    <div className={`p-5 rounded-xl border transition-colors ${alert ? "bg-red-950/40 border-red-800 text-red-200" : "bg-slate-900 border-slate-800 text-slate-100"}`}>
      <div className="flex items-center justify-between mb-2">
        <span className="text-xs text-slate-400 font-mono">{title}</span>
        {icon}
      </div>
      <div className="text-2xl font-bold font-mono tracking-tight">{value}</div>
      <div className="text-[11px] text-slate-500 font-mono mt-1">{subtitle}</div>
    </div>
  );
};
