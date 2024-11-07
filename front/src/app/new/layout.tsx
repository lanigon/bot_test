export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
        <body>
          <a>test hahah</a>        
          {children}
        </body>
    </html>
  );
}
