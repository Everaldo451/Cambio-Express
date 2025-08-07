import Header from "@/components/globals/home"

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