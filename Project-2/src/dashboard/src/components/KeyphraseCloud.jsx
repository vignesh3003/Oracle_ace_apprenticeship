import React from 'react'
import { Tag } from 'lucide-react'

export const KeyphraseCloud = ({ reviews }) => {
  const allPhrases = []
  reviews.forEach(r => {
    if (Array.isArray(r.keyphrases)) {
      allPhrases.push(...r.keyphrases)
    }
  })

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 space-y-4">
      <h2 className="text-lg font-bold text-slate-900 flex items-center gap-2">
        <Tag className="w-5 h-5 text-purple-600" />
        Extracted AI Keyphrases
      </h2>
      <p className="text-xs text-slate-500">Key terms identified by OCI Language AI Service</p>

      <div className="flex flex-wrap gap-2 pt-2">
        {allPhrases.length === 0 ? (
          <span className="text-xs text-slate-400">No keyphrases extracted yet.</span>
        ) : (
          allPhrases.map((phrase, idx) => (
            <span
              key={idx}
              className="bg-slate-100 border border-slate-200 text-slate-700 text-xs font-mono px-2.5 py-1 rounded-md hover:bg-slate-200 transition-colors"
            >
              #{phrase}
            </span>
          ))
        )}
      </div>
    </div>
  )
}
