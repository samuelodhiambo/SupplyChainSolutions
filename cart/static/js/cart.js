$(document).ready(function(){
    $("tbody tr").each(function(key){ 
        $(this).children("td").children(".plus").click(function(){
            let newVal = parseInt($(this).siblings("input").val()) + 1
            $(this).siblings("input").val(newVal)

            var serializedData = {
                'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
                'order_amount': parseInt($(this).siblings("input").val()),
                'id': $("[name='pk']").val(),
            }
            // make POST ajax call
            $.ajax({
                type: 'POST',
                url: "/cart/ajaxAdd/",
                data: serializedData,
                success: function (response) {
                    order = response.instance
                    // $(btn).siblings("input").val(order.order_amount)
                    $("#"+order.id).text(order.total)
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                },
            })

        })

        $(this).children("td").children(".minus").click(function(){
            let newVal = parseInt($(this).siblings("input").val()) - 1
            if ($(this).siblings("input").val() > 1) {
                $(this).siblings("input").val(newVal)
            }

            var serializedData = {
                'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val(),
                'order_amount': parseInt($(this).siblings("input").val()),
                'id': $("[name='pk']").val(),
            }
            // make POST ajax call
            $.ajax({
                type: 'POST',
                url: "/cart/ajaxAdd/",
                data: serializedData,
                success: function (response) {
                    order = response.instance
                    // $(btn).siblings("input").val(order.order_amount)
                    $("#"+order.id).text(order.total)
                },
                error: function (response) {
                    // alert the error if any error occured
                    alert(response["responseJSON"]["error"]);
                },
            })


        })
    })
});