import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "OracleCloudGuard-X | OCI Vault & Security Auditor",
  description: "Automated Cloud Security Compliance Auditor",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
