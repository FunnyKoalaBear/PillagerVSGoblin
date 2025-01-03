points = 0; 

function changeColor(color, id) {

    const button = document.getElementById(id)
    button.style.backgroundColor = color

    if (color == "green") {
        document.querySelector("#answer").innerHTML = "Correct!"
        document.querySelector("#answer").style.color = "green"

        setTimeout(() => {
            document.querySelector("#answer").innerHTML = ""
        }, 2000);

        points = points + 1
        console.log("Points after correct answer in changeColor():", points);  // Log points

    }
    else if (color == "red") {
        document.querySelector("#answer").innerHTML = "Wrong."
        document.querySelector("#answer").style.color = "red"

        setTimeout(() => {
            button.style.backgroundColor = "#d9edff";
        }, 2000);

        setTimeout(() => {
            document.querySelector("#answer").innerHTML = ""
        }, 2000);
    
    }

}

function checkAnswer() {

    const answer = document.getElementById("answerInput").value.trim().toLowerCase();

    if (answer == 'switzerland') {
        document.querySelector("#secondAnswer").innerHTML = "Correct!"
        document.querySelector("#secondAnswer").style.color = "green"
        points = points + 1
        console.log("Points after correct answer in changeColor():", points);  // Log points

        setTimeout(() => {
            document.querySelector("#secondAnswer").innerHTML = ""
        }, 2000);

        setTimeout(() => {
    
            fullMarks()
            
        }, 3000);

    }
    else {
        document.querySelector("#secondAnswer").innerHTML = "Wrong, TRY AGAIN."
        document.querySelector("#secondAnswer").style.color = "red"

        setTimeout(() => {
            document.querySelector("#secondAnswer").innerHTML = ""
        }, 2000);

    }

}


function fullMarks() {

    if (points >= 2) {

        document.getElementById('winner').scrollIntoView({
            behavior: 'smooth', 
            block: 'start'      
        });

    } 
}

