export default function AddButton(props:React.HTMLAttributes<HTMLButtonElement>) {
    const afterStyle = `
        after:absolute 
        after:w-[2px] after:h-[60%] 
        after:left-[50%] after:top-[50%] 
        after:transform-[translate(-50%,-50%)] 
        after:bg-white
    `
    const beforeStyle = `
        before:absolute 
        before:w-[60%] before:h-[2px] 
        before:left-[50%] before:top-[50%] 
        before:transform-[translate(-50%,-50%)] 
        before:bg-white
    `

    return (
        <button 
            {...props}
            className={
                `relative bg-inherit border-[2px] border-solid border-white p-[15px] rounded-[50%] ${afterStyle} ${beforeStyle} hover:cursor-pointer`
            }
        />
    )
}