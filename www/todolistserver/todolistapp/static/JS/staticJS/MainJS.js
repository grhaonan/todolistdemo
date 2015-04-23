/**
 * Created by gr_haonan on 15/4/7.
 */


/**Define Jquery To Post Data**/

function senddata(){
    $('#myModal form').submit(function(){
            $.ajax({
                    type:"POST",
                    data:$('#myModal form').serialize(),
                    url:"{% url "add" %}",
                    cache: false,
                    dataType: "html",
                    success: function(html, textStatus) {
                        $('#todo').replaceWith(html);
                        $('#myModal').modal('hide');
                        $('#myModal form')[0].reset();
                    },
                    error: function (XMLHttpRequest, textStatus, errorThrown) {
                        $('#comment_form form').replaceWith('Your comment was unable to be posted at this time.  We apologise for the inconvenience.');
                    }

                });
            return false;
        });
    }/**end up senddata**/

    $(document).ready(function(){
    senddata();
    })





