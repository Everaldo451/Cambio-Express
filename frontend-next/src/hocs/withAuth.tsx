import React, { ComponentProps } from "react"


export default function withAuth(Component:(props?:any) => React.JSX.Element) {

    return (props:ComponentProps<typeof Component>) => {

        if (!props.user) {
            return <Component {...props}></Component>
        }

        return <Component {...props}></Component>

    }
}