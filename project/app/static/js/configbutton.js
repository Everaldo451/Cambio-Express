const main = document.querySelector("main")
const form = main.querySelector("form")
const buttons = form?.querySelectorAll("button")

if (buttons) {
    for (const button of buttons) {

        button.addEventListener("click",(e) => {
            e.preventDefault()
            console.log(button)
            const parent = e.currentTarget.parentElement

            const input = parent.querySelector("input")
            if (input.readOnly == true) {
                input.readOnly = false
                input.classList.add(["write"])
                console.log(input.classList)
            } else {
                input.readOnly = true
                input.classList.remove(["write"])
                console.log(input.classList)
            }

        })
    }
}



const submmiter = form?.querySelector("input[type='submit']")

if (submmiter) {
    submmiter.addEventListener("click",(e) => {
        e.preventDefault()
        const submitter = e.currentTarget
        const form = submitter.parentElement

        const inputs = form.querySelectorAll("input")

        for (const input of inputs) {

            if (input.classList.contains("write")) {
                return
            }
        }

        form.submit()
    })
}