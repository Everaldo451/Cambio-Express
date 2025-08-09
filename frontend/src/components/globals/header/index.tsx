import React from "react";
import Image from "next/image";
import { redirect } from "next/navigation";
import { getUser } from "@/lib/server/getUser";

import NavLi from "./NavLi";
import NavLink from "./NavLink";
import ImageLink from "./ImageLink";
import Menu from "./Menu";


export default async function Header() {

    const user = await getUser()
    
    async function logout(e:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
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
                        <Menu logout={logout}/>
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