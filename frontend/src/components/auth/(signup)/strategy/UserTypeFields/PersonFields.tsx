import AuthInputContainer from "@/components/auth/styled-components/AuthInputContainer"

export default function PersonFields() {
    return (
        <>
            <AuthInputContainer inputAttrs={{name:"full_name",id:"full_name",required: true}}/>
        </>
    )
}