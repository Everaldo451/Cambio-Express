import React from "react";
import Link from "next/link";
import { Url } from "next/dist/shared/lib/router/router";

export default function NavLink({
    children,
    href,
}:{
    children:React.ReactNode,
    href: Url,
}) {
    return (
        <Link href={href} className="relative block text-black no-underline p-[5px_8px]">
            {children}
        </Link>
    )
}