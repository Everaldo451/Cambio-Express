import React, { HTMLAttributes, useContext } from "react";
import { ComponentProps } from "react";
import Image from "next/image";
import Link from "next/link";
import { Url } from "next/dist/shared/lib/router/router";
import { redirect } from "next/navigation";

//import { UserContext } from "../../main";


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


function NavLi({
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


function NavLink({
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


function ImageLink({
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


function MenuGridLine({
    children
}:{
    children?:React.ReactNode
}) {
    return (
        <div className="bg-black">{children}</div>
    )
}


export default function Header() {

    const user = null
    
    async function logoutFunc(e:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        e.preventDefault()

        try {
            await fetch("/api/auth/logout/",{
                method:"GET",
                credentials:"include"
            })
            redirect("/")
        } catch(e) {
            redirect("/")
        }
    }
    
    return (
        <header className="fixed top-[0] left-[0] w-full font-instrument-sans shadow-[0_0_3px_gray] z-[2]">
            <nav>
                <ul className="flex bg-header p-[5px_10px] m-[0] items-center list-none backdrop-filter-[blur(10px)]">
                    <NavLi>
                        <ImageLink href={"/"}>
                            <Image src={"/images/logo.png"} width={30} height={30} alt="Cambio Express Logo" className="h-[30px] block"/>
                        </ImageLink>
                    </NavLi>
                    {user?
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
                                    <DropdownButton onClick={logoutFunc}>Logout</DropdownButton>
                                </DropdownLi>
                            </ul>
                        </section>
                    :
                        <NavLi>
                            <NavLink href={"/login"}>Login</NavLink>
                        </NavLi>
                    }   
                </ul>
            </nav>
        </header>
    )
    
}