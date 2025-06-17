"use client";
import axios, { AxiosError } from "axios"

function StyledGoogleButton(props:React.HTMLAttributes<HTMLButtonElement>) {
    return (
        <button
            {...props}
            className="flex align-center bg-white p-[5px] mt-[20px] border-solid border-[2px] border-gray-200 rounded-[5px] outline-none hover:cursor-pointer"
        >
            {props.children}
        </button>
    )
}


function Img(props:React.ImgHTMLAttributes<HTMLImageElement>) {
    return (
        <img
            {...props}
            className="w-[20px] mr-[10px]"
        />
    )
}

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
