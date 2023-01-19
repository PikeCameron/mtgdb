// Function to show or hide div based on which radio is selected
function showDiv() {
  [].forEach.call(document.querySelectorAll('[name=divToggle]'), function(button){
    document.getElementById(button.dataset.divid).className = button.checked? '' : 'hidden';
  })
}

// Attach click listeners onload
window.onload = function() {
  [].forEach.call(document.querySelectorAll('[name=divToggle]'), function(button) {
    button.onclick = showDiv;
  })
}