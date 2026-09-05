"use client";

import React, { useState, useEffect } from "react";
import { Header } from "../components/Header";
import { MetricCard } from "../components/MetricCard";
import { LiveChart } from "../components/LiveChart";
import { AlertHistoryTable } from "../components/AlertHistoryTable";
import { Cpu, HardDrive, Network, Bell, RefreshCw } from "lucide-react";

export default function Home() {
  const [metrics, setMetrics] = useState<any[]>([]);
  const [anomalies, setAnomalies] = useState<any[]>([]);

  const loadData = async () => {
    try {
      const [mRes, aRes] = await Promise.all([
        fetch("http://localhost:8000/api/v1/metrics/history"),
        fetch("http://localhost:8000/api/v1/metrics/anomalies")
      ]);
      const mData = await mRes.json();
      const aData = await aRes.json();
      setMetrics(mData || []);
      setAnomalies(aData || []);
    } catch (e) {
      console.error(e);
    }
  };

  useEffect(() => {
    loadData();
    const interval = setInterval(loadData, 5000);
    return () => clearInterval(interval);
  }, []);

  const latestCpu = metrics.length ? `${metrics[0].cpu_utilization_pct}%` : "32.5%";
  const latestRam = metrics.length ? `${metrics[0].memory_utilization_pct}%` : "58.2%";

  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100 font-sans">
      <Header />

      <main className="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8 space-y-8">
        <section className="bg-gradient-to-r from-slate-900 via-slate-800 to-sky-950 rounded-2xl p-6 border border-slate-800 shadow-xl">
          <span className="bg-sky-500 text-white text-[10px] font-mono font-bold px-3 py-1 rounded-full uppercase tracking-wider">
            Oracle ACE Apprentice Showcase Project 3
          </span>
          <h2 className="text-2xl font-extrabold mt-2 text-white">Real-Time Edge-to-Cloud Infrastructure Telemetry System</h2>
          <p className="text-xs text-slate-300 mt-1 max-w-2xl">
            Hosted on <strong>OCI Always Free Ampere A1 Compute (ARM64)</strong>, utilizing <strong>python-oracledb SessionPool</strong> for low-latency writes to Oracle Autonomous DB, statistical Z-score anomaly detection, and instant email alerting via <strong>OCI Notification Service (ONS)</strong>.
          </p>
        </section>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <MetricCard title="CPU UTILIZATION" value={latestCpu} subtitle="Host: oci-ampere-arm-vm-01" icon={<Cpu className="w-5 h-5 text-sky-400" />} />
          <MetricCard title="RAM UTILIZATION" value={latestRam} subtitle="24 GB Ampere Memory Pool" icon={<HardDrive className="w-5 h-5 text-emerald-400" />} />
          <MetricCard title="NETWORK TRAFFIC" value="4.2 MB/s" subtitle="OCI VCN Ingress / Egress" icon={<Network className="w-5 h-5 text-purple-400" />} />
          <MetricCard title="OCI ONS ALERTS" value={anomalies.length.toString()} subtitle="Subscribed Email Topics" alert={anomalies.length > 0} icon={<Bell className="w-5 h-5 text-amber-400" />} />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <LiveChart metrics={metrics} />
          <AlertHistoryTable anomalies={anomalies} />
        </div>
      </main>

      <footer className="bg-slate-900 border-t border-slate-800 py-6 text-center text-xs text-slate-400 font-mono">
        <p>Built for Oracle ACE Apprentice Program • Product Usage Milestone Submission 3</p>
      </footer>
    </div>
  );
}
