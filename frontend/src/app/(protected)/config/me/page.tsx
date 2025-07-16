export default function PersonalDataConfigsPage() {

    const user = {
        first_name: "Mocked",
        email: "mocked@gmail.com"
    }

    return (
        <>
            <p>Username: <span>{user?.first_name}</span></p>
            <p>Email: <span>{user?.email}</span></p>

            <p>Conta Empresarial:</p>
            <ul>
            </ul>
        </>
    )
}