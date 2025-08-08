'use client'
import { useEffect, ReactNode, useRef, HTMLAttributes } from "react";

function FeedbackDisplaySection(
    props:React.DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement>
) {
    return (
        <section
            {...props}
            className="grid grid-cols-[calc(24%_-_(14px/4))] grid-flow-col gap-[calc(4%/3)] m-[0_10px] overflow-hidden"
        >
            {props.children}
        </section>
    )
}

interface FeedDisplayProps {
    children: ReactNode,
    elementIndex: number,
}

export default function FeedbackDisplay({children,elementIndex}:FeedDisplayProps) {

    const sectionRef = useRef<HTMLDivElement|null>(null)

    useEffect(() => {
        console.log(elementIndex)
        if (sectionRef.current) {
            const childrens = sectionRef.current.querySelectorAll(":scope > div")

            const element = childrens[elementIndex]
            console.log(element)
            if (element) {
                element.scrollIntoView({
                    inline:"start",
                    behavior:"smooth"
                })
            }
        }
    },[elementIndex])

    return (
        <FeedbackDisplaySection ref={sectionRef}>
            {children}
        </FeedbackDisplaySection>
    )
}