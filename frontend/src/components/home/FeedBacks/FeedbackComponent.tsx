'use client'
import { HTMLAttributes } from "react";

export interface FeedBack {
    first_name: string,
    date: Date,
    comment:string
}

function FeedbackDiv(
    props:React.DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement>
) {
    return (
        <div
            {...props}
            className="bg-[#BEC1C1] rounded-[20px_0] p-[20px] font-instrument-sans shadow-[7px_10px_10px_var(--box-shadow-theme)]"
        >
            {props.children}
        </div>
    )
}

function FeedbackH5(props:React.HTMLAttributes<HTMLHeadingElement>) {
    return (
        <h5
            {...props}
            className="text-[15px] text-black font-semibold m-[0]"
        >
            {props.children}
        </h5>
    )
}

function FeedbackH6(props:React.HTMLAttributes<HTMLHeadingElement>) {
    return (
        <h6
            {...props}
            className="text-[10px] text-[#5F5F5F] m-[0] font-normal"
        >
            {props.children}
        </h6>
    )
}

function FeedbackParagraph(props:React.HTMLAttributes<HTMLParagraphElement>) {
    return (
        <p
            {...props}
            className="text-[12px] text-black m-[20px_0_30px_0] leading-[1.3]"
        >
            {props.children}
        </p>
    )
}

/*Process Data Components*/

export default function FeedbackComponent({first_name, date, comment}:FeedBack) {

    return (
        <FeedbackDiv>
            <FeedbackH5>{first_name}</FeedbackH5>
            <FeedbackH6>{`${date.getDate()}/${date.getMonth()}/${date.getFullYear()}`}</FeedbackH6>
            <div className="avaliation">
                <FeedbackParagraph>Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Repellendus, consectetur cum natus sunt iure tempora dolor, aliquid, dolorum 
                    praesentium laudantium sequi soluta quibusdam ipsam. Vitae quidem error ipsum velit eos.
                </FeedbackParagraph>
            </div>            
        </FeedbackDiv>  
    )

}