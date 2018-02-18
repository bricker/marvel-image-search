(function() {
  $('#search-btn').click(function() {
    var data = $('#search-input').val()
    $.ajax({
      url: '/search-results',
      data: { 'q': data },
      type: 'GET'
    }).done(function(res) {
      _.each(res, function(image) {
        $('#search-results').append('<img class="marvel-image" src=' + image + '>').slideDown("slow");
      })
    });
  })
})();
