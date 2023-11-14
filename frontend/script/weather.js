window.addEventListener("load", () => {
    startWeather();

})


function startWeather(){
    console.log("Weather started");

    getWeatherData();
    setInterval(getWeatherData, 300000); // henter hvert 5 minutt
}


async function updateText(data){
    console.log(data);
    console.log(data['temp'])
    var temperature = document.getElementById("temp")
    temperature.textContent = data['temp'] + "°C"
}


async function getWeatherData(){
    fetch('/api/weather')
    .then(response => response.json())
    .then(data => updateText(data))
    .catch(error => console.error("Error fetching data:", error));
}
