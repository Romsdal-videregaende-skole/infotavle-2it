async function getJoke(){
    const api = new URL('http://127.0.0.1:5000/joke')

    const response = await fetch(api)

    if (data.Setup !== "Null"){
        console.log(data.Setup, data.Punchline)
    } else{
        console.log(data.Punchline)
    }

    document.getElementById("temp").innerHTML = jPunchline
}
