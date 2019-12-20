$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});

$(function () {
  $('[data-toggle="popover"]').popover()
});

$('body').on('click', '.confirm-btn', function () {
    var dataId = $(this).attr('data-id');
    $('#delete-form-' + dataId).submit();  
});
