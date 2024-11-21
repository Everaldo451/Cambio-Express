import styled from "styled-components";
import { SetStateAction, ReactNode } from "react";
import { FormProps } from "../LoginForm";

const StyledButton = styled.button`
    position: relative;
    background-color: transparent;
    border: none;
    padding: 3px;
    transition: all 0.5s;
    color: white;
    z-index: 1;

    &:before {
        content: "";
        position: absolute;
        background-color: #3F4156;
        width: 100%;
        height: 2px;
        left: 0;
        top: -2px;
    }

    &:after {
        content: "";
        z-index: -10;
        position: absolute;
        background-color: white;
        width: calc(100% + 4px);
        height: 2px;
        top: 100%;
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
    }

`

const StyledDiv = styled.div`
    width: 100%;
    display: grid;
    grid-template-rows: auto;
    grid-auto-columns: repeat(2, 1fr);
    grid-auto-flow: column;
    gap: 8px;
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
            <Button setURL={setURL} url="login">Login</Button>
            <Button setURL={setURL} url="register">Register</Button>
        </StyledDiv>
    )

}

export default ChangeURL