import { ConfigRoute } from "../styled-components";
import { useContext } from "react";
import { UserContext } from "../../../../main";

export default function PersonalData() {

    const [user] = useContext(UserContext)

    return (
        <ConfigRoute>
            <p>Username: <span>{user?.first_name}</span></p>
            <p>Email: <span>{user?.email}</span></p>

            <p>Conta Empresarial:</p>
            <ul>
            </ul>
        </ConfigRoute>
    )
}