setInterval(async function getJoke(){
    
    const api = new URL('http://127.0.0.1:5000/api/joke')

    const response = await fetch(api)

    const data = await response.json()

    if (data.Setup !== null){
       
        document.getElementById("setup").innerHTML = data.Setup;
    }

    document.getElementById("punchline").innerHTML = data.Punchline

    

},15000)