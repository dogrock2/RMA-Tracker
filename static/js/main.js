//** Calls the login modal when the login link is clicked
$("#loginBtn").on('click', function () {
    $("#loginModal").modal("show");
});

$("#loginModalFrm").on("submit", function(e){
    e.preventDefault();
    let inputUser = $("#inputUser").val().trim();
    let inputPwd = $("#inputPassword1").val().trim();

    let cred = {
        inputUser: inputUser,
        inputPwd: inputPwd
    };
    let credentials = JSON.stringify(cred);
    
    $.ajax({
        url: "/verifyLogin",
        type: "POST",
        contentType: "application/json",
        dataType: "json",
        data: credentials,
        success: function(data){},        
        error: function(error){
            $("#loginErr").text(error);
        }
    });
});

//** Change/Reset button on the settings page 
$("#chngBtnPwd").on('click', function () {
    console.log("Button Clicked");
});

//** This is to give fuctionality to radio buttons on the settings page
$("#pwdForm").on('change', function () {
    let radioVal = $('input[name=pwdRadios]:checked').val();
    if (radioVal === 'option1') {
        $("#changePwd1").removeAttr("disabled");
        $("#changePwd2").removeAttr("disabled");
        $("#chngBtnPwd").text("Change");
    } else if (radioVal === 'option2') {
        $("#changePwd1").attr("disabled", "disabled");
        $("#changePwd2").attr("disabled", "disabled");
        $("#chngBtnPwd").text("Reset");
    }
});

//** This executes when the registration page sign in button is pressed. 
$("#regFrm").on("submit", function (e) {
    e.preventDefault();
    let userName = $("#regInputUser").val().trim();
    let inputEmail1 = $("#inputEmail1").val().trim();
    let inputEmail2 = $("#inputEmail2").val().trim();
    let regInputPassword1 = $("#regInputPassword1").val().trim();
    let regInputPassword2 = $("#regInputPassword2").val().trim();

    let dataComp = {
        userName: userName,
        inputEmail: inputEmail1,
        regInputPassword: regInputPassword1
    };

    let dataComp2 = JSON.stringify(dataComp);

    if (inputEmail1 === inputEmail2) {
        $("#emailErr").text(``);
        if (regInputPassword2 === regInputPassword1) {
            $("#pwdErr").text(``);
            $.ajax({
                url: "/addRegistration",
                type: "POST",
                contentType: "application/json",
                dataType: "json",
                data: dataComp2,
                success: function(data){
                    console.log(data);
                    if(data.success){                        
                        $("#regFrm").trigger("reset");
                        $("#msgModal").modal("show");
                    }
                },
                error: function(error){
                    console.log(`Server responded with "${error.responseText}"`);
                    err = error.responseText;
                    if(err === "Username Duplicate")
                        $("#pwdErr").text(`This username is already in use.`);
                    else if (err === "Email Duplicate")
                        $("#pwdErr").text(`This email is already in our database.`);    
                    else    
                        $("#pwdErr").text(error);                    
                }
            });
        } else {
            $("#pwdErr").text(` ERROR: Passwords must match.`);
        }
    } else {
        $("#emailErr").text(` ERROR: Emails must match.`);
    }

});