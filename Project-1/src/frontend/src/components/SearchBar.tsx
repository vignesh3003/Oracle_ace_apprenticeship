"use client";

import React, { useState } from "react";
import { Search, Sparkles, Loader2 } from "lucide-react";
import { searchVectors, SearchResponse } from "../lib/api";
import { SimilarityBadge } from "./SimilarityBadge";

export const SearchBar: React.FC = () => {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState<SearchResponse | null>(null);

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;
    setLoading(true);

    try {
      const res = await searchVectors(query, 5);
      setResults(res);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-semibold text-oracle-dark flex items-center gap-2">
          <Sparkles className="w-5 h-5 text-purple-600" />
          Semantic Natural Language Vector Search
        </h2>
        <span className="text-xs text-gray-400 font-mono">VECTOR_DISTANCE(..., COSINE)</span>
      </div>

      <form onSubmit={handleSearch} className="flex gap-2">
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-gray-400 absolute left-3 top-3.5" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask anything about indexed documents (e.g. 'What are OCI Vision features?')"
            className="w-full pl-9 pr-4 py-2.5 bg-gray-50 border border-gray-300 rounded-lg text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-oracle-red focus:bg-white"
          />
        </div>
        <button
          type="submit"
          disabled={loading || !query.trim()}
          className="bg-oracle-dark hover:bg-oracle-gray text-white text-xs font-semibold px-5 py-2.5 rounded-lg flex items-center gap-2 transition-colors disabled:opacity-50"
        >
          {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : "Run 23ai Query"}
        </button>
      </form>

      {results && (
        <div className="mt-6 space-y-4">
          <div className="flex items-center justify-between text-xs text-gray-500 border-b pb-2 font-mono">
            <span>Execution Engine: <strong className="text-oracle-red">{results.execution_engine}</strong></span>
            <span>Matches Found: {results.results.length}</span>
          </div>

          <div className="space-y-3">
            {results.results.length === 0 ? (
              <div className="text-xs text-gray-500 py-4 text-center">No semantically similar document chunks found.</div>
            ) : (
              results.results.map((res) => (
                <div key={res.chunk_id} className="p-4 bg-gray-50 border border-gray-200 rounded-lg hover:border-oracle-red/40 transition-colors">
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs font-bold text-gray-800 font-mono">
                      📄 {res.document_name} (Chunk #{res.chunk_index})
                    </span>
                    <SimilarityBadge scorePct={res.similarity_score_pct} distance={res.distance} />
                  </div>
                  <p className="text-xs text-gray-700 leading-relaxed font-sans bg-white p-3 rounded border border-gray-100">
                    "{res.chunk_text}"
                  </p>
                </div>
              ))
            )}
          </div>
        </div>
      )}
    </div>
  );
};
