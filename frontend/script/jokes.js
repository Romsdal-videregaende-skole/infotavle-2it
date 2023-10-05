setInterval(async function getJoke(){
    
    const api = new URL('http://127.0.0.1:5000/api/joke')

    const response = await fetch(api)

    const data = await response.json()

    if (data.Setup !== ""){
        console.log(data.Setup, data.Punchline)
    } else{
        console.log(data.Punchline)
    }

    var jSetup= JSON.stringify(data.Setup)       
    var jPunchline = JSON.stringify(data.Punchline)

    document.getElementById("setup").innerHTML = jSetup;
    document.getElementById("punchline").innerHTML = jPunchline
},15000)