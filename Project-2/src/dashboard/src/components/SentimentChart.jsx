import React from 'react'
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from 'recharts'
import { BarChart3 } from 'lucide-react'

export const SentimentChart = ({ reviews }) => {
  const counts = { Positive: 0, Negative: 0, Neutral: 0 }
  reviews.forEach(r => {
    if (counts[r.sentiment] !== undefined) counts[r.sentiment]++
  })

  const data = [
    { name: 'Positive', value: counts.Positive, color: '#10B981' },
    { name: 'Neutral', value: counts.Neutral, color: '#F59E0B' },
    { name: 'Negative', value: counts.Negative, color: '#EF4444' }
  ]

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 space-y-4">
      <h2 className="text-lg font-bold text-slate-900 flex items-center gap-2">
        <BarChart3 className="w-5 h-5 text-blue-600" />
        OCI Language AI Sentiment Breakdown
      </h2>

      <div className="h-56 w-full">
        <ResponsiveContainer width="100%" height="100%">
          <PieChart>
            <Pie
              data={data}
              cx="50%"
              cy="50%"
              innerRadius={50}
              outerRadius={80}
              paddingAngle={5}
              dataKey="value"
            >
              {data.map((entry, index) => (
                <Cell key={`cell-${index}`} fill={entry.color} />
              ))}
            </Pie>
            <Tooltip />
            <Legend />
          </PieChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}
