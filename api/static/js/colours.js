

function generate_colours() {
  console.log("{% url 'api:generate_colours'   %}")
  $('.contentBox').empty()
  $.ajax({
    type: 'get',
    url: '../generate_colours',
    data: {
    },
    dataType: 'json',
    success: function(data) {
    console.log(data);

    for(let i=0; i<data.length; i++){

      let colour = data[i]
      $('.contentBox').append('<div class="colorBox"> <div class="color" style="background-color:'+colour.value+';"></div><p class="code">' +colour.value +'</p></div>');
    }

    }
  })


}
