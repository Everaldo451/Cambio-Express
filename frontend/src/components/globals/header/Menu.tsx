import React, { HTMLAttributes } from "react";
import { ComponentProps } from "react";
import Link from "next/link";

function DropdownLi({
    children
}:{
    children:React.ReactNode
}) {
    return (
        <li className="p-[10px]">
            {children}
        </li>
    )
}

function DropdownLink(attrs:ComponentProps<typeof Link>) {
    return (
        <Link {...attrs} className="block w-full bg-black border-none text-white text-center text-[15px] no-underline hover:cursor-pointer"></Link>
    )
}

function DropdownButton(attrs:HTMLAttributes<HTMLButtonElement>) {
    return (
        <button {...attrs} className="block w-full bg-black border-none text-white text-center text-[15px] no-underline hover:cursor-pointer"></button>
    )
}

function MenuGridLine({
    children
}:{
    children?:React.ReactNode
}) {
    return (
        <div className="bg-black">{children}</div>
    )
}


interface DropdownProps {
    logout: (e:React.MouseEvent<HTMLButtonElement, MouseEvent>) => Promise<void>
}
export default function Menu({logout}:DropdownProps) {
    return (
        <section className="flex items-center relative m-auto self-stretch group">
            <div className="w-[30px] h-[60%] grid gap-[4px] auto-rows-[1fr]">
                <MenuGridLine/>
                <MenuGridLine/>
                <MenuGridLine/>
            </div>
            <ul className="absolute hidden flex-col p-[0] right-[0] top-[100%] list-none bg-black group-hover:flex">
                <DropdownLi>
                    <DropdownLink href="/configurations">Configurations</DropdownLink>
                </DropdownLi>
                <DropdownLi>
                    <DropdownLink href="/investiments">Investiments</DropdownLink>
                </DropdownLi>
                <DropdownLi>
                    <DropdownButton onClick={logout}>Logout</DropdownButton>
                </DropdownLi>
            </ul>
        </section>
    )
}