import React, { HTMLAttributes, useContext } from "react";
import { useRouter } from "next/router";
import { ComponentProps } from "react";
import { UserContext } from "../../main";
import Image from "next/image";
import Link from "next/link";
import Logo from "../../assets/logo.png"
import { Url } from "next/dist/shared/lib/router/router";


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
        <li className="nth-last-1:m-auto">
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
        <Link href={href} className="relative block bg-black no-underline p-[5px 8px]">
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
        <Link href={href} className="relative block bg-black no-underline p-[0]">
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

    const [user,_] = useContext(UserContext)
    const router = useRouter()
    
    async function logoutFunc(e:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        e.preventDefault()

        try {
            await fetch("/api/auth/logout/",{
                method:"GET",
                credentials:"include"
            })
            router.push("/")
        } catch(e) {
            router.push("/")
        }
    }
    
    return (
        <header className="fixed top-[0] left-[0] w-full font-instrument-sans shadow-[0_0_3px_gray] z-[2]">
            <nav>
                <ul className="flex bg-[ #D9D9D9] p-[5px_10px] m-[0] items-center list-none backdrop-filter-[blur(10px)]">
                    <NavLi>
                        <ImageLink href={"/"}>
                            <Image src={Logo} alt="Cambio Express Logo" className="h-[30px] block"/>
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
                            <NavLink href={"/auth"}>Login</NavLink>
                        </NavLi>
                    }   
                </ul>
            </nav>
        </header>
    )
    
}