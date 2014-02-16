// Custom JS

// create referral via ajax request
function createReferral(){
    var dataString = $('form#referral_create').serialize();
    console.log(dataString);
    $.ajax({
        type: "POST",
        url: "/apiv1/referrals/",
        data: dataString,
        success: function(data) {
            console.log(data);
            var html ='<tr><td>'+ data.title +'</td><td>'+ data.slug +'</td><td>'+ data.clicks +'</td><td><a href="#">Edit</a></td><td><a href="#">Delete</a></td></tr>';
            $('.table tbody').append(html);
            var message_html = '<div class="alert alert-info"><a class="close" data-dismiss="alert">×</a><span>' + 'New referral added.' + '</span></div>'
            $('#messages').append(message_html);
        }
     });
     return false;
}