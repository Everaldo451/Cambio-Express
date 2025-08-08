import AuthInputContainer from "@/components/auth/styled-components/AuthInputContainer"

export default function CompanyFields() {
    return (
        <>
            <AuthInputContainer inputAttrs={{name:"name",id:"name",required: true}}/>
            <AuthInputContainer inputAttrs={{name:"CNPJ",id:"CNPJ",required: true}}/>
            <input type="hidden" name="company" required/>
        </>
    )
}