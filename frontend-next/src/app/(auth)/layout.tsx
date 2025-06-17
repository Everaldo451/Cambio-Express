import ChangeRouteButtons from "@/components/auth/ChangeRouteButtons";
import GoogleButton from "@/components/auth/OAuth/GoogleButton";
import { redirect } from "next/navigation";

function MainElement({
    children
}: {
    children:React.ReactNode
}) {
    return (
        <main
            className={`flex flex-col align-center justify-center bg-theme h-[100dvh]`}
        >
            {children}
        </main>
    )
}


export default function AuthLayout({
    children
}:{
    children:React.ReactNode
}) {

    const user = null

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