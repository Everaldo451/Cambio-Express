import { redirect } from "next/navigation";

import MainContentContainer from "@/components/config/MainContentContainer";
import ConfigsNav from "@/components/config/ConfigsNav";
import ConfigsDisplayer from "@/components/config/ConfigsDisplayer";

import StyledLink from "@/components/config/styled-components/StyledLink";


function MainElement(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <main
            {...props}
            className="flex min-h-[100dvh] items-center bg-theme"
        >
            {props.children}
        </main>
    )
}

export default async function ConfigLayout({
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
            <MainContentContainer>

                <section>
                    <ConfigsNav>
                        <StyledLink href={"/config/me"}>
                            Dados Pessoais
                        </StyledLink>
                        <StyledLink href={"/config/security"}>
                            Segurança
                        </StyledLink>
                        <StyledLink href={"/config/signatures"}>
                            Assinaturas
                        </StyledLink>
                    </ConfigsNav>
                </section>
                
                <ConfigsDisplayer>
                    {children}
                </ConfigsDisplayer>
            </MainContentContainer>
        </MainElement>
    )
}