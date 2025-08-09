import React from "react";

export default function NavLi({
    children
}:{
    children:React.ReactNode
}) {
    return (
        <li className="nth-last-1:ml-auto">
            {children}
        </li>
    )
}