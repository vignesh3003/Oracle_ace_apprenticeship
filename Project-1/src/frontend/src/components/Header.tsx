"use client";

import React, { useState } from "react";
import { Database, Cloud, Cpu, Settings } from "lucide-react";
import { OciCredentialsModal } from "./OciCredentialsModal";

export const Header: React.FC = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <header className="bg-oracle-dark border-b border-oracle-gray text-white py-4 px-6 sticky top-0 z-40 shadow-md">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="bg-oracle-red p-2 rounded-lg text-white shadow-lg">
            <Database className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
              OracleDocuAI
              <span className="bg-oracle-red/20 text-oracle-red border border-oracle-red/40 text-xs px-2 py-0.5 rounded-full font-mono font-medium">
                23ai Vector Search
              </span>
            </h1>
            <p className="text-xs text-gray-400">
              OCI Vision AI & Oracle Autonomous Database 23ai Intelligence Hub
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-4">
          <div className="hidden md:flex items-center space-x-2 text-xs bg-oracle-gray/60 px-3 py-1.5 rounded-md border border-gray-700">
            <Cloud className="w-4 h-4 text-oracle-red" />
            <span className="text-gray-300">OCI Vision AI</span>
            <span className="text-gray-500">•</span>
            <Cpu className="w-4 h-4 text-emerald-400" />
            <span className="text-gray-300">VECTOR(384, FLOAT32)</span>
          </div>

          <button
            onClick={() => setIsModalOpen(true)}
            className="flex items-center space-x-1.5 bg-oracle-gray hover:bg-gray-700 text-xs text-gray-200 px-3 py-2 rounded-md border border-gray-600 transition-colors"
          >
            <Settings className="w-3.5 h-3.5 text-oracle-red" />
            <span>OCI Credentials Guide</span>
          </button>
        </div>
      </div>

      <OciCredentialsModal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)} />
    </header>
  );
};
