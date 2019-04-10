function makeRequest(request_body, url) {
    $.ajax({
        url: url,
        dataType: 'json',
        type: 'POST',
        contentType: 'application/json',
        data: request_body,
        success: function (data, textStatus, jQxhr) {
            console.log(data, textStatus, jQxhr);
        },
        error: function (jqXhr, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });
}