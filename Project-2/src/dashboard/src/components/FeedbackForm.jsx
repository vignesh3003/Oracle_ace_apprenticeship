import React, { useState } from 'react'
import { Send, Loader2, CheckCircle2 } from 'lucide-react'

export const FeedbackForm = ({ onSubmissionSuccess }) => {
  const [text, setText] = useState('')
  const [category, setCategory] = useState('Database Services')
  const [loading, setLoading] = useState(false)
  const [successMsg, setSuccessMsg] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!text.trim()) return
    setLoading(true)
    setSuccessMsg('')

    try {
      const res = await fetch('http://localhost:8000/api/v1/analyze', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text,
          customer_id: `cust_${Math.floor(100 + Math.random() * 900)}`,
          category
        })
      })
      const data = await res.json()
      setSuccessMsg(`Processed by OCI Function: ${data.document.sentiment} sentiment (${(data.document.confidence_score * 100).toFixed(0)}%)`)
      setText('')
      onSubmissionSuccess()
    } catch (err) {
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 space-y-4">
      <h2 className="text-lg font-bold text-slate-900 flex items-center gap-2">
        <Send className="w-5 h-5 text-red-600" />
        Submit Customer Review Telemetry
      </h2>
      <p className="text-xs text-slate-500">
        Triggers HTTP API Gateway $\rightarrow$ OCI Functions serverless Python execution $\rightarrow$ OCI Language AI.
      </p>

      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1">Product Category</label>
          <select
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            className="w-full bg-slate-50 border border-slate-300 rounded-lg p-2 text-xs text-slate-800"
          >
            <option>Database Services</option>
            <option>OCI Functions & Serverless</option>
            <option>Cloud Infrastructure & VM</option>
            <option>AI & Machine Learning</option>
          </select>
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-700 mb-1">Review Content</label>
          <textarea
            rows="3"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Type customer review (e.g. 'Oracle Autonomous Database setup was extremely fast and reliable.')"
            className="w-full bg-slate-50 border border-slate-300 rounded-lg p-3 text-xs text-slate-800 focus:bg-white focus:outline-none focus:ring-2 focus:ring-red-500"
          ></textarea>
        </div>

        <button
          type="submit"
          disabled={loading || !text.trim()}
          className="w-full bg-red-600 hover:bg-red-700 text-white text-xs font-bold py-2.5 rounded-lg flex items-center justify-center gap-2 transition-colors disabled:opacity-50"
        >
          {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : "Trigger OCI Function & Analyze"}
        </button>
      </form>

      {successMsg && (
        <div className="bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs p-3 rounded-lg flex items-center gap-2 font-mono">
          <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
          <span>{successMsg}</span>
        </div>
      )}
    </div>
  )
}
