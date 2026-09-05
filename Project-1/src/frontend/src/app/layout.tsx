import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "OracleDocuAI | Oracle Database 23ai & OCI Vision AI",
  description: "Enterprise Document Intelligence & Semantic Vector Search System",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
