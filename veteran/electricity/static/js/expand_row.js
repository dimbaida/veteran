$(document).ready(function() {
    // jQuery click event to toggle row details
    $('tr.expandable-row').click(function() {
        $(this).next('.additional-info').toggle();
    });
});