import { redirect } from "next/navigation";

import { ConfigSection, MenuButtonsContainer, StyledLink,  } from "@/components/config/styled-components";



//import { UserContext } from "../../main";

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
        redirect("/")
    }
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