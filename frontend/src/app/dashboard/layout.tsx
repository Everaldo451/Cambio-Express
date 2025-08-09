import { redirect } from "next/navigation";
import DashboardMenu from "@/components/dashboard/DashboardMenu";
import DashboardMain from "@/components/dashboard/DashboardMain";
import '../globals.css';


export default async function DashboardLayout({
    children
}:{
    children:React.ReactNode
}) {
    const user={}

    if (!user) {
        redirect("/")
    }
    return (
       <div className="flex">
        <DashboardMenu/>
        <DashboardMain>
            {children}
        </DashboardMain>
       </div> 
    )
}