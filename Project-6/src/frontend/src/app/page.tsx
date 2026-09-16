"use client";

import React from "react";
import { Header } from "../components/Header";
import { AuditPanel } from "../components/AuditPanel";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100 font-sans">
      <Header />

      <main className="flex-1 max-w-5xl w-full mx-auto p-4 sm:p-6 lg:p-8 space-y-6">
        <section className="bg-gradient-to-r from-slate-900 via-slate-800 to-emerald-950 rounded-2xl p-6 border border-slate-800 shadow-xl">
          <span className="bg-emerald-600 text-white text-[10px] font-mono font-bold px-3 py-1 rounded-full uppercase tracking-wider">
            Oracle ACE Apprentice Showcase Project 6
          </span>
          <h2 className="text-2xl font-extrabold mt-2 text-white">Automated Infrastructure Security Compliance Auditor</h2>
          <p className="text-xs text-slate-300 mt-1 max-w-2xl">
            Scans OCI resource configurations via <strong>OCI Python SDK</strong>, verifies secret encryption in <strong>OCI Vault (KMS)</strong>, and logs audit compliance telemetry to <strong>Oracle Autonomous Database</strong>.
          </p>
        </section>

        <AuditPanel />
      </main>

      <footer className="bg-slate-900 border-t border-slate-800 py-6 text-center text-xs text-slate-400 font-mono">
        <p>Built for Oracle ACE Apprentice Program • Product Usage Milestone Submission 6</p>
      </footer>
    </div>
  );
}
