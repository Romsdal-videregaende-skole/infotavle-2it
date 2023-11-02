var width = 1; // Initial width
var id; // Variable to store the interval ID

document.addEventListener("DOMContentLoaded", function () {
  // Initial fetch and update
  updateLoadingBar();

  // Subsequent calls every second
  setInterval(updateLoadingBar, 5000);
});

// Function to fetch data from the API
async function fetchData() {
  try {
    const response = await fetch('http://192.168.1.32:5000/friminutt');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.friminutt || 0; // Use the value of "friminutt" or default to 0
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
}

// Function to update the loading bar
function updateLoadingBar() {
  fetchData().then(apiResult => {
    if (apiResult !== null) {
      // Ensure the value is never less than 0
      apiResult = Math.max(0, apiResult);
      
      // Ensure the value is never more than 100
      apiResult = Math.min(100, apiResult);
      
      // Jump directly to the new value without smooth animation
      jumpTo(apiResult);
    }
  });
}

// Function to jump directly to the target value without smooth animation
function jumpTo(targetWidth) {
  var elem = document.getElementById("loading-bar");
  width = targetWidth; // Set the width directly
  elem.style.width = width + "%";
}
