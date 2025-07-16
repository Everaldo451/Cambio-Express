import Header from "@/components/Header"

export default async function App({
    children
}:{
    children:React.ReactNode
}) {
    return (
        <>
            <Header/>
            {children}
        </>
    )
}