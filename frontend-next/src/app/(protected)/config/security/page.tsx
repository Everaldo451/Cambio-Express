import { ConfigRoute } from "@/components/config/styled-components";

export default function Security() {

    const user = {
        first_name: "Mockedname"
    }

    return (
        <ConfigRoute>
            <p>Username: <span>{user?.first_name}</span></p>
        </ConfigRoute>
    )
}