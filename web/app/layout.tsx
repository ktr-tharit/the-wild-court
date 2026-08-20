import type { Metadata, Viewport } from "next";
import { headers } from "next/headers";
import "./globals.css";
import "./game.css";

export const viewport: Viewport = {
  themeColor: "#08110E",
};

export async function generateMetadata(): Promise<Metadata> {
  const requestHeaders = await headers();
  const host = requestHeaders.get("x-forwarded-host") ?? requestHeaders.get("host") ?? "localhost:3000";
  const protocol = requestHeaders.get("x-forwarded-proto") ?? (host.startsWith("localhost") ? "http" : "https");
  const base = new URL(`${protocol}://${host}`);
  const title = "The Wild Court — The First Winter";
  const description = "An identity adventure where winter remembers the pattern of your choices.";
  const socialImage = new URL("/og.png", base).toString();

  return {
    metadataBase: base,
    title,
    description,
    icons: { icon: "/favicon.svg", shortcut: "/favicon.svg" },
    openGraph: { title, description, type: "website", images: [{ url: socialImage, width: 1792, height: 938, alt: "The Wild Court — Winter remembers how you arrived." }] },
    twitter: { card: "summary_large_image", title, description, images: [socialImage] },
  };
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="th"><body>{children}</body></html>;
}
