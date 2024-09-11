const main = document.querySelector("main")
const content = main.querySelector(".introduction")
const container = content?.querySelector(".imgcontainer")
const img = container?.querySelector("img")

const buttons = container?.querySelectorAll("button")

async function fetchData(coin) {

    try {
        const response = await fetch(`/graphs/get/${coin}`)
        const data = await response.json()

        if (img) {
            img.src = data.image
        }

        return
    }
    catch (error) {}
}

fetchData("USD")

if (buttons) {
    for (const button of buttons) {
        const input = button.querySelector("input")
        button.addEventListener("click",(e) => {
            e.preventDefault()
            fetchData(input.value)
        })
    }
}