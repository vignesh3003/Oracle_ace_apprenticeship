"use client";

import React from "react";
import { FileCheck, Calendar, Database, CheckCircle2 } from "lucide-react";
import { Document } from "../lib/api";

interface DocumentCardProps {
  doc: Document;
}

export const DocumentCard: React.FC<DocumentCardProps> = ({ doc }) => {
  return (
    <div className="bg-white border border-gray-200 rounded-xl p-4 shadow-sm hover:shadow-md transition-shadow">
      <div className="flex items-start justify-between">
        <div className="flex items-center space-x-3">
          <div className="bg-oracle-red/10 p-2.5 rounded-lg text-oracle-red">
            <FileCheck className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-sm font-semibold text-gray-900 font-mono truncate max-w-[200px]">
              {doc.document_name}
            </h3>
            <p className="text-[11px] text-gray-500 font-mono">
              Object: {doc.storage_object_name}
            </p>
          </div>
        </div>
        <span className="bg-emerald-50 text-emerald-700 text-[10px] font-mono px-2 py-0.5 rounded border border-emerald-200 flex items-center gap-1">
          <CheckCircle2 className="w-3 h-3" />
          {doc.ocr_status}
        </span>
      </div>

      <div className="mt-4 grid grid-cols-2 gap-2 text-[11px] text-gray-600 font-mono bg-gray-50 p-2.5 rounded-lg border border-gray-100">
        <div>Size: {(doc.file_size_bytes / 1024).toFixed(1)} KB</div>
        <div>OCR Conf: {doc.confidence_score}%</div>
        <div className="col-span-2 flex items-center gap-1 text-gray-500">
          <Calendar className="w-3 h-3" />
          {doc.created_at}
        </div>
      </div>
    </div>
  );
};
