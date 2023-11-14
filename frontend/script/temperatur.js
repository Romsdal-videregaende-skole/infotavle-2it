document.addEventListener("DOMContentLoaded", function (){
    getTemperature()
})


function updateText(temp){
    var temperatur = document.getElementById("temp")
    temperatur.textContent = temp + "°C"

}





function getTemperature(){
    getTemperatureData()
    setInterval(getTemperatureData, 10000)
}

async function getTemperatureData(){

    await fetch('/api/temperature')
    .then(response => response.json())
    .then(data => updateText(data['netatmo']['Temperature']))

}