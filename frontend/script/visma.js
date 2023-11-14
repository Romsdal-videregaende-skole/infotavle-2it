
document.addEventListener("DOMContentLoaded", function (){
  getVisma()

})

function textUpdate(data) {
  console.log("Updating text");
  console.log(getCurrentTime());

  var nesteTime = document.getElementById("fag");
  var teacher = document.getElementById("lærer");

  if (getCurrentTime() !== null) {
      console.log("Setting text");

      nesteTime.textContent = data[getCurrentTime()][0];
      teacher.textContent = data[getCurrentTime()][1];
  } else {

      nesteTime.textContent = "";
      teacher.textContent = "Fri";
  }
}


function getVisma() {
    console.info("Fetching");
    fetchVismaData();  // Call fetchVismaData immediately
    setInterval(fetchVismaData, 1000000);  // Set interval for subsequent calls
}

function fetchVismaData() {
    fetch('/api/visma')
        .then(response => response.json())
        .then(data => textUpdate(data, console.log(data)))
        .catch(error => console.error("Error fetching data:", error));
}



function getCurrentTime(){
    var timeliste = {
        "08:20": "1.time",
        "09:10": "2.time",
        "10:10": "3.time",
        "11:00": "4.time",
        "12:15": "5.time",
        "13:05": "6.time",
        "13:55": "7.time"
      };
      
      // Get the current time
      var currentTime = new Date();
      var currentHours = currentTime.getHours();
      var currentMinutes = currentTime.getMinutes();
      
      // Format the current time as a string in HH:mm format
      var formattedCurrentTime = (currentHours < 10 ? "0" : "") + currentHours + ":" + (currentMinutes < 10 ? "0" : "") + currentMinutes;
      
      // Find the next item in the dictionary
      var nextItem = null;
      for (var key in timeliste) {
        if (key > formattedCurrentTime) {
          nextItem = timeliste[key];
          itemKey = key
          break;
        }
      }
      
      // Output the result
      if (nextItem) {
        console.log(nextItem, " ", itemKey)
        return key
      } else {
        console.error("There are no more items");
        return null
      }

}

