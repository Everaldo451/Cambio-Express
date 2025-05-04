import axios, { AxiosError } from "axios"

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

    return <button onClick={onClick}>Sign with Google</button>
}