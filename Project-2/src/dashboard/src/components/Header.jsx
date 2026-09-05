import React from 'react'
import { Zap, Cloud, Database, Activity } from 'lucide-react'

export const Header = () => {
  return (
    <header className="bg-slate-900 text-white border-b border-slate-800 py-4 px-6 sticky top-0 z-40 shadow-md">
      <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
        <div className="flex items-center space-x-3">
          <div className="bg-red-600 p-2 rounded-lg text-white shadow-lg">
            <Zap className="w-6 h-6" />
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight text-white flex items-center gap-2">
              Serverless Feedback Pulse
              <span className="bg-red-500/20 text-red-400 border border-red-500/40 text-xs px-2 py-0.5 rounded-full font-mono">
                OCI Functions + SODA
              </span>
            </h1>
            <p className="text-xs text-slate-400">
              OCI API Gateway $\rightarrow$ OCI Functions $\rightarrow$ OCI Language AI $\rightarrow$ Autonomous JSON DB (SODA)
            </p>
          </div>
        </div>

        <div className="flex items-center space-x-3 text-xs bg-slate-800/80 px-3 py-1.5 rounded-md border border-slate-700 font-mono">
          <Cloud className="w-4 h-4 text-orange-400" />
          <span>OCI Language AI</span>
          <span className="text-slate-600">•</span>
          <Database className="w-4 h-4 text-emerald-400" />
          <span>SODA REST DB</span>
        </div>
      </div>
    </header>
  )
}
