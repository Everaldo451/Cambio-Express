import Header from "@/components/Header"

export default function App({
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