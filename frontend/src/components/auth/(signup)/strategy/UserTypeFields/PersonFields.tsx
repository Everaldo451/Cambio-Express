import AuthInputContainer from "@/components/auth/styled-components/AuthInputContainer"
import { useState } from "react"

export default function PersonFields() {
    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")

    async function handleFullNameInput(e:React.FormEvent<HTMLInputElement>) {
        const splitedName = e.currentTarget.value.split(" ")
        setFirstName(splitedName[0])
        setLastName(
            prev => 
                splitedName.length>1?splitedName.slice(1).join(" "):prev
        )
    }

    return (
        <>
            <AuthInputContainer 
                inputAttrs={
                    {
                        id:"full_name",
                        name:"full_name",
                        required:false,
                        onInput:handleFullNameInput,
                    }
                }
            />
            <input type="hidden" name="first_name" value={firstName} required/>
            <input type="hidden" name="last_name" value={lastName} required/>
        </>
    )
}