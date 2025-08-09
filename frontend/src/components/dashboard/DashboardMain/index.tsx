export default async function DashboardMain({children}:{children:React.ReactNode}) {
    return (
        <main className="h-dvh bg-[#22272A] grow font-instrument-sans">
            {children}
        </main>
    )
}