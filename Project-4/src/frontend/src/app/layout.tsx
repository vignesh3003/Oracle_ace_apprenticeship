import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "OracleGenAI-RAG | OCI Generative AI & Autonomous DB",
  description: "Enterprise Knowledge Assistant",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
