// VARIABLES

let name = "Vaibhav";
const PI = 3.14;
var age = 22;


// FUNCTION

function add(a, b)
{
return a + b;
}


// MAIN FUNCTION

function runProgram()
{

let output = "";


/* FUNCTION USE */

let sum = add(5, 3);

output += "Addition using function: " + sum + "<br>";



/* CONDITION */

if(age > 25)
{
output += "Age condition: Older than 25 <br>";
}

else if(age > 20)
{
output += "Age condition: Between 20 and 25 <br>";
}

else
{
output += "Age condition: Less than 20 <br>";
}



/* LOOP */

output += "<br>Loop Example (Numbers 1 to 5):<br>";

for(let i=1; i<=5; i++)
{
output += i + "<br>";
}


document.getElementById("result").innerHTML = output;

}