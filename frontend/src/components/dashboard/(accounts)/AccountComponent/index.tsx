import { AccountType } from "@/types"

export default function AccountComponent({id, code, balance}:AccountType) {
    return (
        <article className="bg-[#181B1D] shadow-[0_4px_10px_rgba(0,0,0,0.25)] rounded-[10px_10px_0_0] overflow-hidden">
            <h3 className="bg-[#272B2F] p-[5px] text-center">{code}</h3>
            <div className="p-[10px_20px]">
                <h4 className="text-[12px]">Balance: {balance}</h4>
            </div>
        </article>
    )
}