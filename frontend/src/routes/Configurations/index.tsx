import styled from "styled-components";
import { Navigate } from "react-router-dom";
import { useContext } from "react";
import { UserContext } from "../../main";

const Main = styled.main`
    display: flex;
    align-items: center;
`

const ConfigSection = styled.section`
    width: 80%;
    max-height: 80%;
    padding: 20px;
    display: grid;
    grid-template-columns: auto 1fr;
    grid-template-rows: 1fr;
    box-shadow: 0 6px 10px rgb(200,200,200);
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

function ConfigurationPage() {

    const [user] = useContext(UserContext)

    return (
        <Main>
            {user?
                <ConfigSection>
                    <MenuButtons>

                        <StyledConfigButton>
                            Dados Pessoais
                        </StyledConfigButton>
                        <StyledConfigButton>
                            Segurança
                        </StyledConfigButton>
                        <StyledConfigButton>
                            Assinaturas
                        </StyledConfigButton>

                    </MenuButtons>
                </ConfigSection>
                :
                <Navigate to={"/"}/>
            }
        </Main>
    )
}

export default ConfigurationPage