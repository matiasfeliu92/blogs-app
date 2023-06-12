console.log('hello world');

let separatedArray = $('.category').map(function() {
  return $(this).text().trim();
}).get();
console.log(separatedArray); // ARRAY DE CATEGORIAS DE LOS POSTS MOSTRADOS

$(document).ready(function() {
$("#search").on("input", () => {
    let searchValue = $("#search").val().trim();
    console.log(searchValue);

    $('.posts').hide(); // Hide all posts initially

    separatedArray.forEach(function(category) {
      if (category.includes(searchValue)) {
        console.log(category);
        // Show the corresponding post(s) based on the category
        $('.category:contains("' + category + '")').closest('.posts').show();
      }
    });
  });
});
