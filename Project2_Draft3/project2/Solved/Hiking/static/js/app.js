// from data.js
var minLength = 0;
var maxLength = 0;
var difficulty = "";

var apiResults;

// Build a table every time we call the table
// Clear out table first every time is called
function masterTable(trailData) {
    // Need to select "tbody" in the index.html page using d3
    var tbody = d3.select("tbody");
    tbody.html("");
    trailData.forEach((trailObjects) => {
        var cityName = trailObjects.location.split(',')[0];
        var row = tbody.append("tr");
        // only need value since we already have the keys set-up

            row.append("td").text(trailObjects.name);
            row.append("td").text(cityName);
            row.append("td").text(trailObjects.length);
            row.append("td").text(trailObjects.difficulty);
            row.append("td").text(trailObjects.stars);
    })
}

function handleLengthChange(control) {
    var length = control.value;
    var splitLength = length.split('-');
    minLength = splitLength[0];
    maxLength = splitLength[1];
    console.log("minLength is ", minLength);
    console.log("maxLength is ", maxLength);
}

function handleDifficultyChange(control) {
    difficulty = control.value;
}



d3.json('/api/hiking', function (error,tableData) {

    // pass in tableData to the created function to see on .html page
    masterTable(tableData);

    apiResults = tableData;
})

 // select button and locate the #filter-btn (this is a ID so use # symbol)
 var press = d3.select("#filter-btn");

// activate button (Enter a Date)
press.on("click", function() {
    // prevent page from refreshing (stops the page from clearing out inputs)
    d3.event.preventDefault();
    // use .property("value") to grab value at the time the button is clicked
    var nameInput = d3.select("#trailname").property("value");
    console.log("nameInput", nameInput);
    var cityInput = d3.select("#city").property("value");
    if (cityInput != "") {
        cityInput += ", Colorado";
    }
    console.log("cityInput", cityInput);
    var difficultyInput = difficulty;
    console.log("difficultyInput", difficultyInput);
    var starsInput = d3.select("#stars").property("value");


    // allows for individual filters

    // looping through code for distance
    var filteredData = apiResults;

    if(nameInput) {
        filteredData = filteredData.filter(row => row.name === nameInput);
    }
    if(cityInput) {
        filteredData = filteredData.filter(row => row.location === cityInput);
    }
    if(difficultyInput) {
        filteredData = filteredData.filter(row => row.difficulty == difficultyInput);
    }
    if(starsInput) {
        filteredData = filteredData.filter(row => row.stars == starsInput);
    };
    console.log(filteredData)

    // pass in masterTable again but with newly created filteredData function
    masterTable(filteredData)
})

var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}




