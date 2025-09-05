"use client"
import { AccountType } from "@/types";
import { redirect } from "next/navigation";

export default function AccountComponent({id, currency, balance}:AccountType) {

    async function handleOnClick(_:  React.MouseEvent<HTMLElement, MouseEvent>) {
        redirect(`/dashboard/accounts/${id}/info/`)
    }

    return (
        <article 
            onClick={handleOnClick}
            className="bg-[#181B1D] shadow-[0_4px_10px_rgba(0,0,0,0.25)] rounded-[10px_10px_0_0] overflow-hidden duration-[0.5s] transition-all hover:scale-[1.1] hover:cursor-pointer"
        >
            <h3 className="bg-[#272B2F] p-[5px] text-center">{currency}</h3>
            <div className="p-[10px_20px]">
                <h4 className="text-[12px]">Balance: {balance}</h4>
            </div>
        </article>
    )
}