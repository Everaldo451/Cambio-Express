import Link from "next/link"

export default function StyledLink(props:React.ComponentProps<typeof Link>) {
    return (
        <Link
            {...props}
            className="relative bg-inherit p-[10px] text-[15px] text-center hover:bg-gray-600 hover:cursor-pointer"
        >
            {props.children}
        </Link>
    )
}