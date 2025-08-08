import PersonFields from "./PersonFields";
import CompanyFields from "./CompanyFields";

const strategy = new Map<string, (() => React.JSX.Element)>()
strategy.set('standard', PersonFields)
strategy.set('company', CompanyFields)

interface UserTypeFieldsProps {
    userType: string
}

export default function UserTypeFields({userType}:UserTypeFieldsProps) {
    const FieldsComponent = strategy.get(userType)
    if (FieldsComponent) {
        return <FieldsComponent/>
    }
    return <></>
}