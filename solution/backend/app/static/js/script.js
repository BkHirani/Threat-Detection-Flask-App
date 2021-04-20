document.addEventListener('DOMContentLoaded', function() {
  M.FormSelect.init(document.querySelectorAll('select'), {});
  M.Modal.init(document.querySelectorAll('.modal'), {});
  M.Collapsible.init(document.querySelectorAll('.collapsible'), {});
});


function openmodel(m) {
  var instance = M.Modal.getInstance(m);
  console.log("azeeb")
  instance.open()
}

function changeFunc(name, idx) {
  
  var selectBox = document.getElementById(name);
  var selectedValue = selectBox.options[selectBox.selectedIndex].value;
  if (selectedValue === "datetime") {
    console.log(selectedValue)
    console.log("modal-"+idx)
    var elem = document.getElementById("modal-"+idx);
    var instance = M.Modal.getInstance(elem);
    // console.log("azeeb")
    instance.open()
  }
  
  // alert(selectedValue);
 }



 $('form').submit(function(e) {
  e.preventDefault();
  $.ajax({
     url: "http://127.0.0.1:3000" + $(this).attr('action'),
     type: $(this).attr('method'),
     data: $(this).serialize(),
     success: function(html) {
      alert("refreshing the page")
      window.location.assign("/");
     }
 });
 e.preventDefault();

});


function get(link){
  $.ajax({
      type: "get",
      url: "http://127.0.0.1:3000" + link,
      data: {
      },
      success: function (data){
        window.location.assign("/");
      },
      error: function (xhr, ajaxOptions, thrownError){

      }
  });
  return false;
}


