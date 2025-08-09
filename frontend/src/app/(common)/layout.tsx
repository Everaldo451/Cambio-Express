import Header from "@/components/globals/header"
import "../globals.css";


export default function CommonLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <>
      <Header/>
        {children}
    </>
  )
}
