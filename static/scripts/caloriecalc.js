function caloriecalc(){
  var totalCalories;
  var chickenCPO = 32.57;
  var flourCPG = 3.64;
  var eggCPG = 1.56;
  var oliveOilCPT = 120;
  var chickenOz = document.getElementById("chicken").value;
  var flourBefore = document.getElementById("flour-before").value;
  var flourAfter = document.getElementById("flour-after").value;
  var eggBefore = document.getElementById("egg-before").value;
  var eggAfter = document.getElementById("egg-after").value;
  var oliveOilTbsp = document.getElementById("olive-oil").value;
  var servings = document.getElementById("servings").value;
  var calculate = (((chickenCPO * chickenOz) + (flourCPG * (flourBefore - flourAfter)) + (eggCPG * (eggBefore - eggAfter)) + (oliveOilCPT * oliveOilTbsp)) / (servings)).toFixed(0);
  if (isNaN(calculate)) {
    totalCalories = "Error: Input must be a number (of grams)"
  } else if (calculate < 0) {
    totalCalories = "Error: grams before exceeds grams after"
  } else if (!isFinite(calculate)) {
    totalCalories = "Error: please enter a valid number of servings"
  } else {
    totalCalories = "Total calories: " + (calculate) + " calories per serving"
  }
  document.getElementById("total-calories").innerHTML = totalCalories;
}
