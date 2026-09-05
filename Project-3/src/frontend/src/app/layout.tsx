import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "OracleTelemetryX | OCI Ampere Compute & ONS Alerting",
  description: "Real-Time Edge-to-Cloud Infrastructure Telemetry System",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
