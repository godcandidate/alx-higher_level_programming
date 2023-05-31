$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, status){
    $(data.results).each(function() {
        $("UL#list_movies").append("<li>" + this.title + "</li>");
        });
  });
