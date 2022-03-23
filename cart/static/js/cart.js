$(document).ready(function(){
    $("tbody tr").each(function(key){ 
        $(this).children("td").children(".plus").click(function(){
            let newVal = parseInt($(this).siblings("input").val()) + 1
            $(this).siblings("input").val(newVal)

            var serializedData = {
                'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
                'order_amount': parseInt($(this).siblings("input").val())
            }
            // make POST ajax call
            $.ajax({
                type: 'POST',
                url: "/cart/ajaxAdd/",
                data: serializedData,
                success: function (response) {
                    // on successfull creating object
                    // 1. clear the form.
                    $("#friend-form").trigger('reset');
                    // 2. focus to nickname input 
                    $("#id_nick_name").focus();

                    // display the newly friend to table.
                    var instance = JSON.parse(response["instance"]);
                    var fields = instance[0]["fields"];
                    $("#my_friends tbody").prepend(
                        `<tr>
                        <td>${fields["nick_name"]||""}</td>
                        <td>${fields["first_name"]||""}</td>
                        <td>${fields["last_name"]||""}</td>
                        <td>${fields["likes"]||""}</td>
                        <td>${fields["dob"]||""}</td>
                        <td>${fields["lives_in"]||""}</td>
                        </tr>`
                    )
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                }
            })

        })

        $(this).children("td").children(".minus").click(function(){
            let newVal = parseInt($(this).siblings("input").val()) - 1
            if ($(this).siblings("input").val() > 1) {
                $(this).siblings("input").val(newVal)
            }
        })
    })
});