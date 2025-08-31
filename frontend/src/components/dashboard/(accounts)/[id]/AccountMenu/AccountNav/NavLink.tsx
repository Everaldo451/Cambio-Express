import { ComponentProps } from "react";
import Link from "next/link";

export default async function NavLink(props:ComponentProps<typeof Link>) {
    return (
        <Link {...props} className="block p-[10px_20px] hover:bg-[#585348] text-white text-[14px] text-center">
            {props.children}
        </Link>
    )
}