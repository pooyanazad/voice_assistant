$(document).ready(function() {
    $('#start-button').click(function() {
        $('#listening-status').text('Listening...');
        $.ajax({
            url: '/process',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ command: 'listen' }),
            success: function(response) {
                $('#response').text(response.response);
                $('#listening-status').text('');
            }
        });
    });

    $('#stop-button').click(function() {
        $('#listening-status').text('Stopping...');
        $.ajax({
            url: '/process',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ command: 'stop' }),
            success: function(response) {
                $('#response').text(response.response);
                $('#listening-status').text('');
            }
        });
    });
});
