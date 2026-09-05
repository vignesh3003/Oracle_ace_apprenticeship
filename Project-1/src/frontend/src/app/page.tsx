"use client";

import React, { useState, useEffect } from "react";
import { Header } from "../components/Header";
import { FileUploader } from "../components/FileUploader";
import { SearchBar } from "../components/SearchBar";
import { DocumentCard } from "../components/DocumentCard";
import { fetchDocuments, Document } from "../lib/api";
import { Database, FileText, Cpu, CheckCircle } from "lucide-react";

export default function Home() {
  const [documents, setDocuments] = useState<Document[]>([]);
  const [loadingDocs, setLoadingDocs] = useState(true);

  const loadDocs = async () => {
    try {
      const data = await fetchDocuments();
      setDocuments(data);
    } catch (e) {
      console.error(e);
    } finally {
      setLoadingDocs(false);
    }
  };

  useEffect(() => {
    loadDocs();
  }, []);

  return (
    <div className="min-h-screen flex flex-col bg-gray-50 text-gray-900 font-sans">
      <Header />

      <main className="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 lg:p-8 space-y-8">
        {/* Banner Section */}
        <section className="bg-gradient-to-r from-oracle-dark via-oracle-gray to-oracle-accent rounded-2xl p-6 sm:p-8 text-white shadow-xl">
          <div className="max-w-3xl space-y-3">
            <span className="bg-oracle-red text-white text-[11px] font-mono font-bold px-3 py-1 rounded-full uppercase tracking-wider">
              Oracle ACE Apprentice Showcase Project
            </span>
            <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
              Multimodal OCR & AI Vector Search with Oracle Database 23ai
            </h2>
            <p className="text-xs sm:text-sm text-gray-300 leading-relaxed">
              Upload unstructured PDFs or images into <strong>OCI Object Storage</strong>, extract text via <strong>OCI Vision AI</strong>, and execute low-latency <strong>384-dimensional cosine vector searches</strong> natively in <strong>Oracle Autonomous Database 23ai</strong>.
            </p>
          </div>
        </section>

        {/* Core Interactive Section */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <FileUploader onUploadSuccess={loadDocs} />
          <SearchBar />
        </div>

        {/* Document Catalog */}
        <section className="space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-bold text-oracle-dark flex items-center gap-2">
              <FileText className="w-5 h-5 text-oracle-red" />
              Indexed Documents Catalog ({documents.length})
            </h3>
            <span className="text-xs text-gray-400 font-mono">Oracle ADB 23ai Master Table</span>
          </div>

          {loadingDocs ? (
            <div className="text-xs text-gray-500 py-6 text-center">Loading document catalog...</div>
          ) : documents.length === 0 ? (
            <div className="bg-white border border-gray-200 rounded-xl p-8 text-center text-xs text-gray-500">
              No documents indexed yet. Upload a PDF or image above to initiate the pipeline.
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {documents.map((doc) => (
                <DocumentCard key={doc.id} doc={doc} />
              ))}
            </div>
          )}
        </section>
      </main>

      <footer className="bg-oracle-dark border-t border-oracle-gray py-6 text-center text-xs text-gray-400 font-mono">
        <p>Built for Oracle ACE Apprentice Program • Product Usage Milestone Submission 1</p>
      </footer>
    </div>
  );
}
