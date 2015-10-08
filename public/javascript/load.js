$(function() {
  $("#get-started").on("click", function(event) {
    $("#upload>textarea").fadeOut(function() {
      $("#upload>textarea").text("");
      $("#upload>p").fadeIn();
    });
  })

  var dropzone = new Dropzone("div#upload",
    {
      url: "/upload",
      paramName: "image"
    }
  );

  dropzone.on("complete", function(file) {
    dropzone.removeFile(file);
  });

  dropzone.on("success", function(file, response) {
    $("#upload>p").fadeOut(function() {
      $("#upload>textarea").text(response);
      $("#upload>textarea").fadeToggle();
    });
  });


});
