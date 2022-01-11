$(document).ready(function () {
    setTimeout(function(){ $('.message').hide('show'); }, 3000);
    $('#id_sub_category').change(function () {
        $.ajax({
            url: document.location.origin+"/category/subcategory/filter/",
            type: 'post',
            data:{
              'id': $('#id_sub_category').val(),
              'csrfmiddlewaretoken':$('[name=csrfmiddlewaretoken]').val()
            },
            success: function(data) {
            $('#id_brand').empty();
                $('#id_brand').append('<option value="" selected="">---------</option>');
                arr = $.parseJSON(data.data); //convert to javascript array
                console.log(arr);
                $.each(arr,function(key,value){
                var text = '<option value="'+value.pk+'">'+value.fields.brand_name+'</option>'
                    $('#id_brand').append(text);
                });
            },
            failure: function(data) {
                alert('Got an error dude');
            }
        });
    });
})