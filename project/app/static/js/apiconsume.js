const main = document.querySelector("main")
const content = main.querySelector(".introduction")
const information = content?.querySelector(".imgcontainer")
const img = information?.querySelector("img")


async function fetchData() {
    const protocol = window.location.protocol
    const host = window.location.host
    console.log(host,protocol)

    try {
        const response = await fetch(`/graphs/get/USD`)

        const data = await response.json()
        
        console.log(data)

        if (img) {
            img.src = data.image
        }
    }
    catch (error) {}
}


console.log(fetchData())