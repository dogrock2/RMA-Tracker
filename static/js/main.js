
$("#loginBtn").on('click', function(){
    $("#loginModal").modal("show");
    console.log("click");
});


$("#chngBtnPwd").on('click', function(){
    console.log("Button Clicked");
}) ;

$("#pwdForm").on('change', function() {
    let radioVal = $('input[name=pwdRadios]:checked').val();  
    if(radioVal === 'option1'){
        $("#changePwd1").removeAttr("disabled");
        $("#changePwd2").removeAttr("disabled");
        $("#chngBtnPwd").text("Change");
    } else if(radioVal === 'option2'){ 
        $("#changePwd1").attr("disabled", "disabled");
        $("#changePwd2").attr("disabled", "disabled");
        $("#chngBtnPwd").text("Reset");
    }
 });
