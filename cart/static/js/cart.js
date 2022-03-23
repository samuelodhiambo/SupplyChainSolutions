$(document).ready(function(){
    $("tbody tr").each(function(key){ 
        $(this).children("td").children(".plus").click(function(){
            let newVal = parseInt($(this).siblings("input").val()) + 1
            $(this).siblings("input").val(newVal)
        })

        $(this).children("td").children(".minus").click(function(){
            let newVal = parseInt($(this).siblings("input").val()) - 1
            if ($(this).siblings("input").val() > 1) {
                $(this).siblings("input").val(newVal)
            }
        })
    })
});