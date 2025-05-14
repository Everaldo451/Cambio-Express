import axios, { AxiosError } from "axios"
import styled from "styled-components"

const StyledGoogleButton = styled.button`
    margin-top: 20px;
    display: flex;
    align-items: center;
    padding: 5px;
    background-color: white;
    outline: none;
    border: 2px solid gray;
    border-radius: 5px;

    &:hover {
        cursor: pointer;
    }
`
const Img = styled.img`
    width: 20px;
    margin-right: 10px;
`

export default function GoogleButton() {

    async function onClick(_:React.MouseEvent<HTMLButtonElement>) {
        try {
            const response = await axios.get("/api/auth/oauth/")
            if (response.status != 200) {
                throw new AxiosError("A error has ocurred", "500", response.config, response.request, response)
            }

            const data = response.data
            console.log(data)
            const authorization_url = data["authorization_url"]
            window.location.assign(authorization_url)
        } catch (error) {
            console.log(error)
        }
    }
    
    return (
        <StyledGoogleButton onClick={onClick}>
            <Img src="https://developers.google.com/identity/images/g-logo.png" alt="Google"/>
            <span>Entrar com Google</span>
        </StyledGoogleButton>
    )
}
