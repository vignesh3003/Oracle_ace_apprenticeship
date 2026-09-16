import React, { useState, useEffect } from 'react'
import { Header } from './components/Header'
import { MediaUploader } from './components/MediaUploader'

export default function App() {
  const [history, setHistory] = useState([])
  const loadHistory = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/v1/transcribe/list')
      const data = await res.json()
      setHistory(data || [])
    } catch (e) { console.error(e) }
  }
  useEffect(() => { loadHistory() }, [])

  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100 font-sans">
      <Header />
      <main className="flex-1 max-w-5xl w-full mx-auto p-6 space-y-6">
        <section className="bg-gradient-to-r from-slate-900 to-sky-950 p-6 rounded-2xl border border-slate-800">
          <span className="bg-sky-600 text-white text-[10px] font-mono px-3 py-1 rounded-full uppercase">
            Oracle ACE Apprentice Showcase Project 5
          </span>
          <h2 className="text-xl font-bold mt-2">Multimodal Audio Transcriber via OCI Speech AI Service</h2>
        </section>
        <MediaUploader onComplete={loadHistory} />
      </main>
    </div>
  )
}
