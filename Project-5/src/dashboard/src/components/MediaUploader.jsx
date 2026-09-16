import React, { useState } from 'react'
import { Upload, Loader2, FileAudio } from 'lucide-react'

export const MediaUploader = ({ onComplete }) => {
  const [file, setFile] = useState(null)
  const [loading, setLoading] = useState(false)
  const [res, setRes] = useState(null)

  const handleUpload = async () => {
    if (!file) return
    setLoading(true)
    const formData = new FormData()
    formData.append('file', file)
    try {
      const response = await fetch('http://localhost:8000/api/v1/transcribe/upload', {
        method: 'POST',
        body: formData
      })
      const data = await response.json()
      setRes(data)
      onComplete()
    } catch (e) { console.error(e) }
    finally { setLoading(false) }
  }

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 space-y-4">
      <h2 className="text-base font-bold text-white flex items-center gap-2">
        <Upload className="w-5 h-5 text-sky-400" /> Upload Media Stream (Audio/Video)
      </h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="text-xs text-slate-300" />
      {file && (
        <button onClick={handleUpload} disabled={loading} className="bg-sky-600 px-4 py-2 text-xs rounded text-white flex items-center gap-2">
          {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : "Transcribe with OCI Speech AI"}
        </button>
      )}
      {res && (
        <div className="bg-slate-850 p-4 rounded text-xs space-y-2 border border-slate-700">
          <div className="font-bold text-emerald-400">Transcription Complete ({res.confidence_score}%)</div>
          <div className="text-slate-300">{res.transcript}</div>
        </div>
      )}
    </div>
  )
}
