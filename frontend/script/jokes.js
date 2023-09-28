async function getJoke(){
    const api = new URL('http://127.0.0.1:5500/joke')

    const response = await fetch(api)

    const data = await response.json()

    console.log(data.Setup, data.Delivery)

}

