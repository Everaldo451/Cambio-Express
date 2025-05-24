import { ConfigRoute } from "../styled-components";
import { useContext } from "react";
import { UserContext } from "../../../../main";

export default function Security() {

    const [user] = useContext(UserContext)

    return (
        <ConfigRoute>
            <p>Username: <span>{user?.first_name}</span></p>
        </ConfigRoute>
    )
}