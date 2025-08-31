"use client"
import { redirect } from "next/navigation";

export default function AccountBlackMask() {
    async function handleOnClick(_:  React.MouseEvent<HTMLElement, MouseEvent>) {
            redirect(`/dashboard/accounts/`)
        }
    return (
        <div 
            onClick={handleOnClick}
            className="fixed right-[0] top-[0] bg-[rgba(0,0,0,0.3)] h-dvh w-dvw z-[2]"
        ></div>
    )
}