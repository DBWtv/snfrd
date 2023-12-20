function file_form(element, course_id) {
    let lecture_id = element.parentElement.id;

    let form = fileForm(lecture_id);
    $('.table-responsive').empty();
    $('.table-responsive').append(form);
    $('.table-responsive').append($('<br>'));
}

function fileForm(lecture_id) {
    let form = $('<form class="addFileForm"></form>');
    let lecture_id_input = $('<input type="hidden" name="lecture_id" id="lecture_id">');
    let name = $('<input type="text" name="name" id="name">');
    let input = $('<input type="file" name="file" id="file" required>');
    let button = $('<button class="btn btn-primary" id="addFileSubmit">add</button>');

    input.on('change', function() {
        if (!name.val()) {
            name.val(this.files[0].name);
        }
    });

    button.on('click', function() {
        let formData = new FormData(form[0]);
        formData.append('csrfmiddlewaretoken', getCookie('csrftoken'));
        let xhr = new XMLHttpRequest();
        xhr.open('POST', '/class/api/add_file/', false);
        xhr.send(formData);
        if (xhr.status != 201) {
            throw new Error(xhr.status + ': ' + xhr.statusText);
        }
        document.location.reload();
    });

    lecture_id_input.val(lecture_id);
    form.append(name);
    form.append(input);
    form.append(button);
    form.append(lecture_id_input);

    return form;
}
