import styled from "styled-components";
import { Navigate } from "react-router-dom";
import { ReactNode, SetStateAction, useContext, useState } from "react";
import DadosPessoais from "./ConfigRoutes/DadosPessoais";
import Seguranca from "./ConfigRoutes/Segurança";
import { UserContext } from "../../main";

interface ButtonProps {
    children: ReactNode,
    configElement: JSX.Element,
    setElement: React.Dispatch<SetStateAction<JSX.Element|null>>,
}

const Main = styled.main`
    display: flex;
    align-items: center;
    background-color: ${props => props.theme.bgColor};
`

const ConfigSection = styled.section`
    background-color: ${props => props.theme.divColor};
    width: 80%;
    max-height: 80%;
    padding: 20px;
    display: grid;
    grid-template-columns: auto 1fr;
    grid-template-rows: 1fr;
    box-shadow: 0 6px 10px ${props => props.theme.boxShadowColor};
    border-radius: 15px;
    margin: auto;
`

const MenuButtons = styled.section`
    position: relative;
    display: grid;
    grid-template-columns: 1fr;
    grid-auto-rows: auto;
    grid-auto-flow: row;
    overflow: auto;
    background-color: rgb(240, 240, 240);

    &:after {
        content: "";
        position: absolute;
        width: 2px;
        height: 100%;
        background-color:black;
        right: 0;
    }
`

export const ConfigRoute = styled.section`
    padding: 15px;
`

const StyledConfigButton = styled.button`
    position: relative;
    padding: 10px;
    font-size: 15px;
    background-color: inherit;
    border: none;

    &:hover {
        background-color: lightgray;
        cursor: pointer;
    }

    & img {
        position: absolute;
    }
`

function ConfigButton({children,configElement, setElement}:ButtonProps) {

    return (
        <StyledConfigButton onClick={(e) => {setElement(configElement)}}>
            {children}
        </StyledConfigButton>
    )


}

function ConfigurationPage() {

    const [user] = useContext(UserContext)
    const [element, setElement] = useState<JSX.Element|null>(null)

    return (
        <Main>
            {user?
                <ConfigSection>
                    <MenuButtons>

                        <ConfigButton setElement={setElement} configElement={<DadosPessoais/>}>
                            Dados Pessoais
                        </ConfigButton>
                        <ConfigButton setElement={setElement} configElement={<Seguranca/>}>
                            Segurança
                        </ConfigButton>
                        <StyledConfigButton>
                            Assinaturas
                        </StyledConfigButton>

                    </MenuButtons>
                    {element?
                        <section>
                            {element}
                        </section>
                    :null}
                </ConfigSection>
                
                :
                <Navigate to={"/"}/>
            }
        </Main>
    )
}

export default ConfigurationPage