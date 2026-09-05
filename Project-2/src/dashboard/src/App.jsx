import React, { useState, useEffect } from 'react'
import { Header } from './components/Header'
import { FeedbackForm } from './components/FeedbackForm'
import { SentimentChart } from './components/SentimentChart'
import { KeyphraseCloud } from './components/KeyphraseCloud'
import { LiveFeed } from './components/LiveFeed'

export default function App() {
  const [reviews, setReviews] = useState([])

  const fetchReviews = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/v1/feedback')
      const data = await res.json()
      setReviews(data.documents || [])
    } catch (e) {
      console.error(e)
    }
  }

  useEffect(() => {
    fetchReviews()
  }, [])

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900 font-sans">
      <Header />

      <main className="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8 space-y-8">
        <section className="bg-gradient-to-r from-slate-900 via-slate-800 to-red-950 rounded-2xl p-6 text-white shadow-xl">
          <span className="bg-red-600 text-white text-[10px] font-mono font-bold px-3 py-1 rounded-full uppercase tracking-wider">
            Oracle ACE Apprentice Showcase Project 2
          </span>
          <h2 className="text-2xl font-extrabold mt-2">Serverless Microservice Sentiment Analytics Pipeline</h2>
          <p className="text-xs text-slate-300 mt-1 max-w-2xl">
            Event-driven serverless architecture using OCI API Gateway, OCI Functions (Python / Fn Project), OCI Language AI, and Oracle Autonomous JSON Database (SODA REST API).
          </p>
        </section>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="space-y-8">
            <FeedbackForm onSubmissionSuccess={fetchReviews} />
            <SentimentChart reviews={reviews} />
          </div>

          <div className="lg:col-span-2 space-y-8">
            <KeyphraseCloud reviews={reviews} />
            <LiveFeed reviews={reviews} />
          </div>
        </div>
      </main>

      <footer className="bg-slate-900 border-t border-slate-800 py-6 text-center text-xs text-slate-400 font-mono">
        <p>Built for Oracle ACE Apprentice Program • Product Usage Milestone Submission 2</p>
      </footer>
    </div>
  )
}
