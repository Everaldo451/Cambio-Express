import NavLink from "./NavLink"
import { AccountType } from "@/types"

export default function AcccountNav({id}:{id:Pick<AccountType, "id">}) {
    return (
        <div className="bg-[#423E36]">
            <ul className="flex justify-center gap-[15px] p-[0_20px] m-[0] list-none">
                <li>
                    <NavLink href={`/dashboard/accounts/${id}/info`}>Info</NavLink>
                </li>
                <li>
                    <NavLink href={`/dashboard/accounts/${id}/deposit`}>Deposit</NavLink>
                </li>
                <li>
                    <NavLink href={`/dashboard/accounts/${id}/withdraw`}>Withdraw</NavLink>
                </li>
                <li>
                    <NavLink href={`/dashboard/accounts/${id}/convert`}>Convert</NavLink>
                </li>
            </ul>
        </div>
    )
}