import React from "react";
import Link from "next/link";
import { Url } from "next/dist/shared/lib/router/router";

export default function ImageLink({
    children,
    href,
}:{
    children:React.ReactNode,
    href: Url,
}) {
    return (
        <Link href={href} className="relative block bg-transparent no-underline p-[0]">
            {children}
        </Link>
    )

}