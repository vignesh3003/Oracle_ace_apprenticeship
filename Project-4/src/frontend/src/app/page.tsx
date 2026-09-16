"use client";

import React from "react";
import { Header } from "../components/Header";
import { ChatBox } from "../components/ChatBox";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100 font-sans">
      <Header />

      <main className="flex-1 max-w-5xl w-full mx-auto p-4 sm:p-6 lg:p-8 space-y-6">
        <section className="bg-gradient-to-r from-slate-900 via-slate-800 to-purple-950 rounded-2xl p-6 border border-slate-800 shadow-xl">
          <span className="bg-purple-600 text-white text-[10px] font-mono font-bold px-3 py-1 rounded-full uppercase tracking-wider">
            Oracle ACE Apprentice Showcase Project 4
          </span>
          <h2 className="text-2xl font-extrabold mt-2 text-white">Enterprise Knowledge Assistant via OCI Generative AI</h2>
          <p className="text-xs text-slate-300 mt-1 max-w-2xl">
            Leveraging <strong>OCI Generative AI Service (Cohere Command R+ / Meta Llama 3 models)</strong> via Python OCI SDK, storing structured conversation history in <strong>Oracle Autonomous Database</strong>.
          </p>
        </section>

        <ChatBox />
      </main>

      <footer className="bg-slate-900 border-t border-slate-800 py-6 text-center text-xs text-slate-400 font-mono">
        <p>Built for Oracle ACE Apprentice Program • Product Usage Milestone Submission 4</p>
      </footer>
    </div>
  );
}
