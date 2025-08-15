'use client'
import { useState, useEffect } from "react";
import { apiAxios } from "@/lib/client/apiAxios";

import FeedbackDisplay from "./FeedbackDisplay";
import FeedbackComponent from "./FeedbackComponent";

import RightArrow from "./Arrow/RightArrow";
import LeftArrow from "./Arrow/LeftArrow";

export interface FeedBack {
    first_name: string,
    date: Date,
    comment:string
}

/*HTML Css Components*/

function Section(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <section
            {...props}
            className="bg-theme p-[60px_40px] font-instrument-sans"
        >
            {props.children}
        </section>
    )
}

function H2(props:React.HTMLAttributes<HTMLHeadingElement>) {
    return (
        <h2
            {...props}
            className="text-white m-[0] text-[24px] font-instrument-sans"
        >
            {props.children}
        </h2>
    )
}

function GridDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="grid grid-cols-[auto_1fr_auto] grid-flow-col mt-[30px]"
        >
            {props.children}
        </div>
    )
}

export async function getFeedBacks() {
        try{
            const response = await apiAxios.get("/feedbacks/search/")
            const responseData = response.data

            const data=[
                {first_name:"João", date: new Date(), comment: "asadasd"},
                {first_name:"Maria", date: new Date(), comment: "asadasd"},
                {first_name:"Rafaela", date: new Date(), comment: "asadasd"},
                {first_name:"José", date: new Date(), comment: "asadasd"},
            ]

            if (responseData satisfies FeedBack[]) {
                responseData.forEach((value:FeedBack) => {data.push(value)})
            }
            return data
    } catch(_) {return []}
}
export default function FeedBacks() {

    const user = {
        first_name: "Mocked name"
    }
    const [feedbacks, setFeedBacks] = useState<FeedBack[]>([])
    const [element, setElement] = useState<number>(0)

    useEffect(() => {
        const feedbacks = getFeedBacks()
        feedbacks.then((value) => setFeedBacks(value))
    },[])

    return (
        <Section>
            <H2>Comentários</H2>
            <GridDiv>
                <LeftArrow 
                    imgProps={{src: "/images/triangle.png"}}
                    setElement={setElement}
                />
                <FeedbackDisplay elementIndex={element}>
                    {
                        user && feedbacks?.filter((feedback) => feedback.first_name == user.first_name).length==0?
                            <FeedbackComponent first_name={user.first_name} comment="adsad" date={new Date()}/>
                        :null
                    }
                    {
                        feedbacks.map((feedback, idx) => 
                            <FeedbackComponent 
                                key={idx}
                                first_name={feedback.first_name} 
                                date={feedback.date} 
                                comment={feedback.comment}
                            />
                        )   
                    }
                </FeedbackDisplay>
                <RightArrow
                    imgProps={{src: "/images/triangle.png"}}
                    setElement={setElement} 
                    feedbacks={feedbacks}
                />
            </GridDiv>
        </Section>
    )
}