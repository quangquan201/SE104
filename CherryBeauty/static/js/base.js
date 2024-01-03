/*=================================Header===========================================*/
function register(){
    window.location.href = '/register';
}
function signin(){
  window.location.href = '/login';
}








/*Chatbox=========================================================================*/
var listtuvanvien = ['Nguyễn Thị Cẩm Tiên', 'Quang Thanh Quân'];


function randomValueFromArray(array) {
    const random = Math.floor(Math.random() * array.length);
    return array[random];
}

function moForm() {
    document.getElementById('tuvanvien').innerHTML = randomValueFromArray(listtuvanvien);
    document.getElementById("myForm").style.display = "block";
    buttonchatbox.style.visibility = 'hidden';
  }

  function dongForm() {
    document.getElementById("myForm").style.display = "none";
    buttonchatbox.style.visibility = 'visible';
  }

const msg = document.querySelector('textarea[name="msg"]');

msg.oninvalid = function(event) {
	event.target.setCustomValidity('Nhập lời nhắn trước khi bắt đầu chat để tư vấn viên có thể hỗ trợ bạn nhanh hơn');
}
