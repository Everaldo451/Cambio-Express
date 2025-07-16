import React, { useEffect, ComponentProps } from "react"
import { useRouter } from "next/router"


export default function withAuth(Component:(props?:any) => React.JSX.Element) {

    return (props:ComponentProps<typeof Component>) => {

        if (!("user" in props) || props.user) {
            return <Component {...props}></Component>
        }

        const router=useRouter()
            
        useEffect(() => {
            router.push("/")
        },[router])
        return <></>
    }
}