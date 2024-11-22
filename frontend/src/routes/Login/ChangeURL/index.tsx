import styled from "styled-components";
import { SetStateAction, ReactNode } from "react";
import { FormProps } from "../LoginForm";

const StyledButton = styled.button`
    position: relative;
    background-color: #8C8A6C;
    border: none;
    border-top: 2px solid white;
    border-bottom: 2px solid white;
    padding: 3px;
    transition: all 0.5s;
    color: white;
    z-index: 1;

    &:before {
        content: "";
        position: absolute;
        background-color: white;
        width: 2px;
        height: 0;
        top: -2px;
        right: -2px;
        transition: all 0.5s;
    }

    &:after {
        content: "";
        position: absolute;
        background-color: white;
        borde: 2px solid white;
        width: 2px;
        height: 0;
        top: calc(100% + 2px);
        left: -2px;
        transition: all 0.5s;
    }

    &:hover {
        cursor: pointer;
        transform: scale(1.1);

        &:after {
            height: calc(100% + 4px);
            top: -2px;
        }

        &:before{   
            height: calc(100% + 4px);
        }
    }

`

const StyledDiv = styled.div`
    width: 100%;
    display: grid;
    grid-template-rows: auto;
    grid-template-columns: repeat(2, 1fr);
    grid-auto-flow: column;
    gap: 20px;
`

interface ChangeURLProps {
    children?: ReactNode,
    setURL: React.Dispatch<SetStateAction<FormProps['url']>>,
    url?: FormProps['url']
}


function Button({children,setURL,url}:ChangeURLProps) {

    return <StyledButton onClick={(e) => {url?setURL(url):null}}>{children?children:""}</StyledButton>
    
}

function ChangeURL({setURL}:ChangeURLProps) {

    return (
        <StyledDiv>
            <Button setURL={setURL} url="login">Entrar</Button>
            <Button setURL={setURL} url="register">Registrar</Button>
        </StyledDiv>
    )

}

export default ChangeURL