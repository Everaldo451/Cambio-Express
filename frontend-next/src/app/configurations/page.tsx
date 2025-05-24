import { ReactNode, SetStateAction, useContext, useEffect, useState } from "react";
import { useRouter } from "next/router";

import { ConfigSection, MenuButtonsContainer, StyledConfigButton,  } from "./_components/styled-components";

import PersonalData from "./_components/ConfigutionSections/PersonalData";
import Security from "./_components/ConfigutionSections/Security";

import { UserContext } from "../../main";


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


function ConfigButton({children,configElement, setElement}:ButtonProps) {

    return (
        <StyledConfigButton onClick={(_:React.MouseEvent<HTMLButtonElement, MouseEvent>) => {setElement(configElement)}}>
            {children}
        </StyledConfigButton>
    )


}

function ConfigurationPage() {

    const [user] = useContext(UserContext)

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
                    <ConfigButton setElement={setElement} configElement={<PersonalData/>}>
                        Dados Pessoais
                    </ConfigButton>
                    <ConfigButton setElement={setElement} configElement={<Security/>}>
                        Segurança
                    </ConfigButton>
                    <StyledConfigButton>
                        Assinaturas
                    </StyledConfigButton>
                </MenuButtonsContainer>
                
                {element?
                    <section>
                        {element}
                    </section>
                :null}
            </ConfigSection>
        </MainElement>
    )
}

export default ConfigurationPage