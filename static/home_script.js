function create(){
    let destination = document.querySelector(".search-input")?.value;
    let days = document.querySelector(".Days")?.value;
    if (destination === '' & days== ''){
        document.querySelector('#warnings').innerHTML='Enter all inputs to continue';
        return 
    }
    else{
        document.querySelector('#warnings').innerHTML='';
    let element = document.querySelector(".hide");
    if(element.classList.contains("hide")){
        element.classList.remove('hide');
        element.classList.add("positionaldiv");
    }
    document.querySelector("#resd").innerHTML=`${destination}`;
    document.querySelector('#resday').innerHTML=`${days}`;
    console.log("Print");
}
}
function save(){
    let element = document.getElementById("save_form");
    let destination =document.querySelector("#resd").textContent;
    let days = document.querySelector("#resday").textContent;
    console.log(destination,days)
    let formdata = { destination:destination,
        days:days,
        distance:element.distance.value,
        date:element.date.value,
        transportation:element.transportation.value,
        hotels:element.hotels.value,
        activities:element.activities.value,
        trip_cost:element.trip_cost.value,
        remarks:element.remarks.value,
        visiting_places:element.visiting_places.value,
    };
    console.log(formdata)
    fetch("/saveplan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify(formdata)
    })
    .then(response => response.json())
    .then(data => console.log("Success:", data),alert("Details successfully saved in the database"))
    .catch(error => console.error("Error:", error));
}
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        document.cookie.split(";").forEach(cookie => {
            let [name, value] = cookie.trim().split("=");
            if (name === "csrftoken") {
                cookieValue = value;
            }
        });
    }
    return cookieValue;
}