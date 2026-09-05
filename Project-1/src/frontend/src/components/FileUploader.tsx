"use client";

import React, { useState } from "react";
import { Upload, FileText, CheckCircle2, AlertCircle, Loader2 } from "lucide-react";
import { uploadDocument, UploadResponse } from "../lib/api";

interface FileUploaderProps {
  onUploadSuccess: () => void;
}

export const FileUploader: React.FC<FileUploaderProps> = ({ onUploadSuccess }) => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<UploadResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
      setResult(null);
      setError(null);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await uploadDocument(file);
      setResult(res);
      setFile(null);
      onUploadSuccess();
    } catch (err: any) {
      setError(err.message || "Failed to process document");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
      <h2 className="text-lg font-semibold text-oracle-dark mb-1 flex items-center gap-2">
        <Upload className="w-5 h-5 text-oracle-red" />
        Document Ingestion Pipeline
      </h2>
      <p className="text-xs text-gray-500 mb-4">
        Upload PDF/Images $\rightarrow$ Extract OCR via OCI Vision AI $\rightarrow$ Index 384-dim Vectors in Oracle 23ai DB
      </p>

      <div className="border-2 border-dashed border-gray-300 hover:border-oracle-red rounded-lg p-6 text-center transition-colors bg-gray-50/50">
        <input
          type="file"
          id="fileInput"
          accept=".pdf,.png,.jpg,.jpeg,.txt"
          onChange={handleFileChange}
          className="hidden"
        />
        <label htmlFor="fileInput" className="cursor-pointer flex flex-col items-center">
          <FileText className="w-10 h-10 text-gray-400 mb-2" />
          <span className="text-sm font-medium text-gray-700">
            {file ? file.name : "Click or drag document here"}
          </span>
          <span className="text-xs text-gray-400 mt-1">Supports PDF, PNG, JPG, JPEG (Max 10MB)</span>
        </label>
      </div>

      {file && (
        <div className="mt-4 flex items-center justify-between bg-blue-50 border border-blue-200 rounded-lg p-3">
          <div className="text-xs text-blue-900 font-mono truncate">
            {file.name} ({(file.size / 1024).toFixed(1)} KB)
          </div>
          <button
            onClick={handleUpload}
            disabled={loading}
            className="bg-oracle-red hover:bg-red-700 text-white text-xs font-semibold px-4 py-2 rounded-lg flex items-center gap-2 transition-colors disabled:opacity-50"
          >
            {loading ? (
              <>
                <Loader2 className="w-4 h-4 animate-spin" />
                OCI Vision Processing...
              </>
            ) : (
              <>Process & Index</>
            )}
          </button>
        </div>
      )}

      {error && (
        <div className="mt-4 bg-red-50 border border-red-200 text-red-700 text-xs p-3 rounded-lg flex items-center gap-2">
          <AlertCircle className="w-4 h-4 shrink-0" />
          <span>{error}</span>
        </div>
      )}

      {result && (
        <div className="mt-4 bg-emerald-50 border border-emerald-200 text-emerald-900 rounded-lg p-4 text-xs space-y-2">
          <div className="flex items-center gap-2 font-bold text-emerald-800">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
            {result.message}
          </div>
          <div className="grid grid-cols-2 gap-2 text-gray-700 font-mono mt-2">
            <div>Doc ID: #{result.document_id}</div>
            <div>Confidence: {result.confidence_score}%</div>
            <div>Vector Chunks: {result.total_chunks}</div>
            <div>Services: {result.oracle_services_invoked.join(", ")}</div>
          </div>
        </div>
      )}
    </div>
  );
};
