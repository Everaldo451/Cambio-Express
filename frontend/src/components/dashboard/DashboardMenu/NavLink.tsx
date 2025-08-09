import { ComponentProps } from "react";
import Link from "next/link";

export default async function NavLink(props:ComponentProps<typeof Link>) {
    return (
        <Link {...props} className="p-[10px_20px] hover:bg-[#3F484D] text-white text-[14px] text-center">
            {props.children}
        </Link>
    )
}