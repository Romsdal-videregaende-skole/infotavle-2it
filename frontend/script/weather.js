document.addEventListener('DOMContentLoaded', () => {
    console.log("test");
    getWeatherData();
    setInterval(getWeatherData, 300000); // henter hvert 5 minutt
})


function updateText(data){
    console.log(data['temp'])
    var temperature = document.getElementById("temp")
    temperature.textContent = data['temp'] + "°C"
}


function getWeatherData(){
    fetch('/api/weather')
    .then(response => response.json())
    .then(data => updateText(data))
    .catch(error => console.error("Error fetching data:", error));
}