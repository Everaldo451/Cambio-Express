import { ReactNode, SetStateAction, useEffect, useState } from "react";
import { useRouter } from "next/router";

import { ConfigSection, MenuButtonsContainer, StyledLink,  } from "@/components/config/styled-components";



//import { UserContext } from "../../main";


interface ButtonProps {
    children: ReactNode,
    configElement: React.JSX.Element,
    setElement: React.Dispatch<SetStateAction<React.JSX.Element|null>>,
}

function MainElement(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <main
            {...props}
            className="flex align-center bg-theme"
        >
            {props.children}
        </main>
    )
}

export default function ConfigLayout({
    children
}:{
    children:React.ReactNode
}) {

    const user={}

    if (!user) {
        const router=useRouter()

        useEffect(() => {
            router.push("/")
        },[router])
        return <></>
    }
    const [element, setElement] = useState<React.JSX.Element|null>(null)
    return (
        <MainElement>
            <ConfigSection>

                <MenuButtonsContainer>
                    <StyledLink href={"/config/me"}>
                        Dados Pessoais
                    </StyledLink>
                    <StyledLink href={"/config/security"}>
                        Segurança
                    </StyledLink>
                    <StyledLink href={"/config/signatures"}>
                        Assinaturas
                    </StyledLink>
                </MenuButtonsContainer>
                
                <section>
                    {children}
                </section>
            </ConfigSection>
        </MainElement>
    )
}