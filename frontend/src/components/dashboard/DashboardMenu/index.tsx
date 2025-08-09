import NavLink from "./NavLink"
import VipResourceNavLink from "./VipResourceNavLink"

async function Aside({children}:{children:React.ReactNode}) {
    return (
        <aside 
        className="h-dvh bg-[#22272A] p-[20px_0] shadow-[4px_0px_5px_#778892] z-[2] font-instrument-sans"
        >
            {children}
        </aside>
    )
}

export default async function DashboardMenu() {
    return (
        <Aside>
            <nav className="flex flex-col gap-[30px]">
                <NavLink href={'/dashboard/accounts'}>Accounts</NavLink>
                <NavLink href={'/dashboard/portfolio'}>Portfolio</NavLink>
                <VipResourceNavLink href={'/dashboard/analytics'}>Analytics</VipResourceNavLink>
            </nav>
        </Aside>
    )
}