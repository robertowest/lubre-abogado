$(document).on('click', '.confirm-delete', function () {
    $("#confirmDeleteModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmDeleteButtonModal', function () {
    var caller = $("#confirmDeleteButtonModal").closest(".modal").attr("caller-id");
    window.location = $("#".concat(caller)).attr("href");
});
