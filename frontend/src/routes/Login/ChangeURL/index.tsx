import styled from "styled-components";
import { SetStateAction, ReactNode } from "react";
import { FormProps } from "../LoginForm";

const StyledButton = styled.button`

    background-color: white;
    border: 1px solid black;
    transition: all 0.5s;

    &:hover {
        cursor: pointer;
        background-color: gray;
        color: white;
    }

`

const StyledDiv = styled.div`
    width: 100%;
    display: grid;
    grid-template-rows: auto;
    grid-auto-columns: repeat(2, 1fr);
    grid-auto-flow: column;
    gap: 2px;
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