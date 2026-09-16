import React from 'react'
import { Mic, Cloud, Database } from 'lucide-react'

export const Header = () => {
  return (
    <header className="bg-slate-900 border-b border-slate-800 py-4 px-6 sticky top-0 z-40">
      <div className="max-w-7xl mx-auto flex justify-between items-center">
        <div className="flex items-center space-x-3">
          <div className="bg-sky-600 p-2 rounded-lg text-white"><Mic className="w-6 h-6" /></div>
          <div>
            <h1 className="text-xl font-bold text-white">OCI MediaStream-AI</h1>
            <p className="text-xs text-slate-400">OCI Speech AI Service & OCI Object Storage Transcriber</p>
          </div>
        </div>
      </div>
    </header>
  )
}
