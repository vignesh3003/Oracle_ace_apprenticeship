import React from 'react'
import { Database, Clock, Smile, Frown, Meh } from 'lucide-react'

export const LiveFeed = ({ reviews }) => {
  const getSentimentIcon = (sentiment) => {
    if (sentiment === 'Positive') return <Smile className="w-4 h-4 text-emerald-500" />
    if (sentiment === 'Negative') return <Frown className="w-4 h-4 text-red-500" />
    return <Meh className="w-4 h-4 text-amber-500" />
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-bold text-slate-900 flex items-center gap-2">
          <Database className="w-5 h-5 text-emerald-600" />
          Autonomous JSON DB SODA Collection Feed
        </h2>
        <span className="text-xs text-slate-400 font-mono">Collection: feedback_collection</span>
      </div>

      <div className="space-y-3 max-h-96 overflow-y-auto pr-1">
        {reviews.map((r) => (
          <div key={r.id} className="p-4 bg-slate-50 border border-slate-200 rounded-lg hover:border-slate-300 transition-colors">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-2">
                {getSentimentIcon(r.sentiment)}
                <span className="text-xs font-bold text-slate-800 font-mono">
                  {r.sentiment} ({(r.confidence_score * 100).toFixed(0)}%)
                </span>
                <span className="text-[10px] bg-slate-200 text-slate-700 px-2 py-0.5 rounded font-mono">
                  {r.category}
                </span>
              </div>
              <div className="flex items-center gap-1 text-[10px] text-slate-400 font-mono">
                <Clock className="w-3 h-3" />
                {r.timestamp}
              </div>
            </div>
            <p className="text-xs text-slate-700 font-sans leading-relaxed mb-2 font-medium">
              "{r.raw_text}"
            </p>
            <div className="text-[10px] text-slate-500 font-mono bg-white p-2 rounded border border-slate-100">
              SODA Doc ID: {r.id} | Customer: {r.customer_id}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
