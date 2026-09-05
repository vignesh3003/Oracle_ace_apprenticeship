"use client";

import React from "react";

interface SimilarityBadgeProps {
  scorePct: number;
  distance: number;
}

export const SimilarityBadge: React.FC<SimilarityBadgeProps> = ({ scorePct, distance }) => {
  let badgeColor = "bg-emerald-100 text-emerald-800 border-emerald-300";
  if (scorePct < 70) badgeColor = "bg-amber-100 text-amber-800 border-amber-300";
  if (scorePct < 40) badgeColor = "bg-red-100 text-red-800 border-red-300";

  return (
    <div className={`inline-flex items-center gap-1.5 text-xs font-mono font-medium px-2.5 py-1 rounded-full border ${badgeColor}`}>
      <span>Cosine Sim: {scorePct}%</span>
      <span className="text-[10px] opacity-75">(Dist: {distance})</span>
    </div>
  );
};
