"use client";

import React, { useState } from "react";
import { Send, Loader2, Bot, User } from "lucide-react";

interface Message {
  role: "user" | "assistant";
  content: string;
  model?: string;
  latency?: number;
}

export const ChatBox: React.FC = () => {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      role: "assistant",
      content: "Hello! I am your OCI Generative AI Knowledge Assistant powered by Cohere Command R+ and Meta Llama 3 models on Oracle Cloud. Ask me anything about OCI architecture, security, or database features!",
      model: "cohere.command-r-plus"
    }
  ]);

  const handleSend = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim()) return;

    const userMsg = prompt.trim();
    setPrompt("");
    setMessages((prev) => [...prev, { role: "user", content: userMsg }]);
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/api/v1/genai/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: userMsg })
      });
      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.response,
          model: data.model_id,
          latency: data.latency_ms
        }
      ]);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 flex flex-col h-[600px] shadow-xl">
      <div className="flex-1 overflow-y-auto space-y-4 pr-2">
        {messages.map((m, idx) => (
          <div key={idx} className={`flex items-start gap-3 ${m.role === "user" ? "justify-end" : "justify-start"}`}>
            {m.role === "assistant" && (
              <div className="bg-purple-600/20 text-purple-400 p-2 rounded-lg border border-purple-500/30">
                <Bot className="w-5 h-5" />
              </div>
            )}
            <div className={`p-4 rounded-xl max-w-2xl text-xs leading-relaxed ${m.role === "user" ? "bg-purple-600 text-white" : "bg-slate-800 text-slate-200 border border-slate-700"}`}>
              <p className="whitespace-pre-line">{m.content}</p>
              {m.model && (
                <div className="mt-2 text-[10px] opacity-75 font-mono flex items-center gap-2 border-t border-slate-700/50 pt-1">
                  <span>Model: {m.model}</span>
                  {m.latency && <span>• Latency: {m.latency}ms</span>}
                </div>
              )}
            </div>
            {m.role === "user" && (
              <div className="bg-slate-700 text-slate-300 p-2 rounded-lg">
                <User className="w-5 h-5" />
              </div>
            )}
          </div>
        ))}
      </div>

      <form onSubmit={handleSend} className="mt-4 flex gap-2 pt-4 border-t border-slate-800">
        <input
          type="text"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Ask OCI Generative AI a question..."
          className="flex-1 bg-slate-850 border border-slate-700 rounded-lg px-4 py-2.5 text-xs text-white focus:outline-none focus:ring-2 focus:ring-purple-500"
        />
        <button
          type="submit"
          disabled={loading || !prompt.trim()}
          className="bg-purple-600 hover:bg-purple-700 text-white text-xs font-semibold px-5 py-2.5 rounded-lg flex items-center gap-2 transition-colors disabled:opacity-50"
        >
          {loading ? <Loader2 className="w-4 h-4 animate-spin" /> : <Send className="w-4 h-4" />}
        </button>
      </form>
    </div>
  );
};
