'use client'
import { SetStateAction } from "react";

import { FeedBack } from "../FeedbackComponent"

interface ArrowProps {
    imgProps: React.ImgHTMLAttributes<HTMLImageElement>
    onClick: (_:React.MouseEvent<HTMLButtonElement, MouseEvent>) => void,
}

export interface FeedbackArrowProps {
    feedbacks: FeedBack[],
    imgProps: React.ImgHTMLAttributes<HTMLImageElement>,
    setElement: React.Dispatch<SetStateAction<number>>,
}

export default function Arrow({imgProps, onClick}:ArrowProps) {

    return (
        <button onClick={onClick}>
            <img 
                {...imgProps}
                className={
                    `w-[20px] m-[auto_0] ${imgProps.className?imgProps.className:null}`
                }
            />
        </button>
    )
}