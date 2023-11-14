setInterval(async function getJoke(){
    document.getElementById("setup").innerHTML = "";
    document.getElementById("punchline").innerHTML = "";

    const response = await fetch("/api/joke")

    const data = await response.json()

    if (data.Setup !== null){
       
        document.getElementById("setup").innerHTML = data.Setup;
    }

    document.getElementById("punchline").innerHTML = data.Punchline

    

},15000)