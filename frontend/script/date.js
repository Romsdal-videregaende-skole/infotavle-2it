

function startdate () {
    // Get current date
    const currentDate = new Date();

    // Days of the week
    const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    // Months of the year
    const monthsOfYear = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

    // Get day, date, and month
    const day = daysOfWeek[currentDate.getDay()];
    const date = currentDate.getDate();
    const month = monthsOfYear[currentDate.getMonth()];

    // Display the result
    const dateDisplay = document.getElementById('dateDisplay');
    dateDisplay.textContent = `${day}  ${date}  ${month}`;

}