import { ComponentProps } from "react";
import Link from "next/link";

async function Span({
    children
}: {
    children: React.ReactNode
}) {
    return (
        <span 
        className="text-[#E5CB00] ml-[10px] p-[2px_4px] border-[2px] border-solid border-[#E5CB00] rounded-[5px]">
            {children}
        </span>
    )
}

export default async function VipResourceNavLink(props:ComponentProps<typeof Link>) {
    return (
        <Link {...props} className="p-[10px_20px] hover:bg-[#3F484D] text-[#E5CB00] text-[14px] text-center">
            {props.children}
            <Span>VIP</Span>
        </Link>
    )
}