window.dccFunctions = window.dccFunctions || {};
window.dccFunctions.priceParser = function(value) {
     return `$${value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",")}`;
}