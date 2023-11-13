setInterval(async function getJoke(){
    document.getElementById("setup").innerHTML = "";
    document.getElementById("punchline").innerHTML = "";
    const api = new URL('/api/joke')

    const response = await fetch(api)

    const data = await response.json()

    if (data.Setup !== null){
       
        document.getElementById("setup").innerHTML = data.Setup;
    }

    document.getElementById("punchline").innerHTML = data.Punchline

    

},15000)