import AuthInputContainer from "@/components/auth/styled-components/AuthInputContainer"
import UserTypeForm from "./UserTypeForm"

export default function PersonFields() {
    return (
        <UserTypeForm userTypeField="client">
            <AuthInputContainer 
                inputAttrs={
                    {id:"first_name",name:"first_name",required:false,}
                }
            />
            <AuthInputContainer 
                inputAttrs={
                    {id:"last_name",name:"last_name",required:false,}
                }
            />
        </UserTypeForm>
    )
}