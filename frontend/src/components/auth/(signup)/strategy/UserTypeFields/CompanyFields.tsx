import AuthInputContainer from "@/components/auth/styled-components/AuthInputContainer"
import UserTypeForm from "./UserTypeForm"

export default function CompanyFields() {
    return (
        <UserTypeForm userTypeField="company">
            <AuthInputContainer 
                inputAttrs={
                    {name:"name",id:"name",required:false}
                }
            />
            <AuthInputContainer 
                inputAttrs={
                    {name:"CNPJ",id:"CNPJ",required:false}
                }
            />
        </UserTypeForm>
    )
}