import ChangeRouteButtons from "@/components/auth/ChangeRouteButtons";
import GoogleButton from "@/components/auth/OAuth/GoogleButton";
import { redirect } from "next/navigation";
import { getUser } from "@/lib/server/getUser";

function MainElement({
    children
}: {
    children:React.ReactNode
}) {
    return (
        <main
            className={`flex flex-col items-center justify-center bg-theme h-[100dvh]`}
        >
            {children}
        </main>
    )
}


export default async function AuthLayout({
    children
}:{
    children:React.ReactNode
}) {
    const user = await getUser()
    if (user) {
        redirect("/")
    }
    else {
        return (
            <MainElement>
                <ChangeRouteButtons/>
                {children}
                <GoogleButton/>
            </MainElement>
        )
    }
}