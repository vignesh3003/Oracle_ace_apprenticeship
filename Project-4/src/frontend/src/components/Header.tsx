"use client";

import React from "react";
import { Bot, Sparkles, Database, Cloud } from "lucide-react";

export const Header: React.FC = () => {
  return (
    <header className="bg-slate-900 border-b border-slate-800 py-4 px-6 sticky top-0 z-40">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="bg-purple-600 p-2 rounded-lg text-white">
            <Bot className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold text-white flex items-center gap-2">
              OracleGenAI-RAG
              <span className="bg-purple-500/20 text-purple-400 border border-purple-500/40 text-xs px-2 py-0.5 rounded-full font-mono">
                Cohere Command R+
              </span>
            </h1>
            <p className="text-xs text-slate-400">
              OCI Generative AI Service $\rightarrow$ Oracle Autonomous Database Chat History
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-3 text-xs bg-slate-800/80 px-3 py-1.5 rounded-md border border-slate-700 font-mono">
          <Sparkles className="w-4 h-4 text-purple-400" />
          <span>OCI GenAI Inference</span>
          <span className="text-slate-600">•</span>
          <Database className="w-4 h-4 text-emerald-400" />
          <span>Autonomous DB</span>
        </div>
      </div>
    </header>
  );
};
