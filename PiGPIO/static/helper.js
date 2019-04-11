function makeRequest(request_body, url, callback) {
    $.ajax({
        url: url,
        dataType: 'json',
        type: 'POST',
        contentType: 'application/json',
        data: request_body,
        success: function (data, textStatus, jQxhr) {
            if (typeof callback !== 'undefined') {
                callback(false, data, textStatus, jQxhr);
            }
        },
        error: function (jqXhr, textStatus, errorThrown) {
            if (typeof callback !== 'undefined') {
                callback(true, errorThrown, textStatus, jqXhr);
            }
        }
    });
}