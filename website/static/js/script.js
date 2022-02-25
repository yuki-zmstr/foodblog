var foodID = '';
var comment = '';

$(document).ready(function() {

  $( "#bw" ).click(function(){
    var element = document.body;
    element.classList.toggle("dark-mode");
  });

  // recipe pop up
  $popup = $('.popup');
  $(document).mousemove(function(){
    $popup.each(function() {
      var $this = $(this)
      var to_pop = "#" + $this.data('name') + "-popup";
      var $to_pop = $(to_pop)
      $this.hover(function(){
        $to_pop.fadeIn(300);
      }, function() {
        $to_pop.fadeOut(300)
      })
    })
  })


  $('.popup').mouseover(function(){
    foodID = this.id;
    // console.log(foodID)
  })

});


function sendFoodInfo(){
  // if user isn't logged in display box
  if (document.getElementById('login') != null) {
    // console.log('please log in')
    alert('Please log in to leave a comment.\nログインして下さい。')
  } else {
    var foodInfo = {
      'id': foodID,
      'comment': $('#comment-'+foodID).val()
    }
    if (foodInfo['comment'] == '') {
      alert('Comment box is empty.\nコメントを入力して下さい。')
    } else {
      fetch('/processFoodInfo', {
        method: 'POST',
        body: JSON.stringify(foodInfo)
      }).then((_res) => {
        window.location.href = '/';
      })
    }

    // const request = new XMLHttpRequest()
    // request.open('POST', `/processFoodInfo/${JSON.stringify(foodInfo)}`)
    // request.onload = () => {
    //   const flaskMessage = request.responseText
    //   // console.log(flaskMessage)
    // }
    // request.send()
  }

}

function deleteComment(commentID) {
  fetch('/delete-comment', {
      method: 'POST',
      body: JSON.stringify({commentId: commentID})
  }).then((_res) => {
      window.location.href = '/';
  })
}