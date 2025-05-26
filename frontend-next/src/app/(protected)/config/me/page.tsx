import { ConfigRoute } from "@/components/config/styled-components";

export default function PersonalDataPage() {

    const user = {
        first_name: "Mocked",
        email: "mocked@gmail.com"
    }

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