export default function SecurityConfigsPage() {
    
    const user = {
        first_name: "Mockedname"
    }

    return (
        <>
            <p>Username: <span>{user?.first_name}</span></p>
        </>
    )
}