(function() {
  $('#search-btn').click(function() {
    var data = $('#search-input').val()
    $.ajax({
      url: '/search-results',
      data: { 'q': data },
      type: 'GET'
    }).done(function(res) {
      var $results = $('#search-results');
      $results.empty().hide();
      _.each(res, function(image) {
        $results.append('<img class="marvel-image" src=' + image + '>').slideDown("slow");
      })
    });
  })
})();
