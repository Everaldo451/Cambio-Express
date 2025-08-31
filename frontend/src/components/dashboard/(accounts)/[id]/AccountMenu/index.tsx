import AcccountNav from "./AccountNav"
import AccountRouteDisplay from "./AccountRouteDisplay"
import { AccountType } from "@/types"

export default function AccountMenu({
    accountId,
    children
}: {
    accountId: Pick<AccountType, "id">
    children: React.ReactNode
}) {
    return (
        <div className="fixed left-[50%] top-[50%] translate-[-50%] z-[3]">
            <AcccountNav id={accountId}/>
            <AccountRouteDisplay>
                {children}
            </AccountRouteDisplay>
        </div>
    )
}