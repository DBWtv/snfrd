
function sendLectureForm(data) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/class/api/add_lecture/', false);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(data));
    if (xhr.status != 201) {
        alert(`Error ${xhr.status}: ${xhr.responseText}`);
    }
    else {
        location.reload();
    }
}


function renderLectureForm(position) {
    let form = $(`<form id = "lecture-form:${position.week_id}:${position.day}"></form>`);
    form.append($(`<div class="form-group"><label for = "lecture-date:${position.week_id}:${position.day}">Дата</label>`));
    form.append($(`<input id = "lecture-date:${position.week_id}:${position.day}" type="date" name="date class="form-control"" required></div>`));
    form.append($(`<div class="form-group"><label for = "lecture-title:${position.week_id}:${position.day}">Название</label>`));
    form.append($(`<input id = "lecture-title:${position.week_id}:${position.day}" type="text" name="title" class="form-control" required></div>`));
    form.append($(`<button type="submit" id="addLecture" >Добавить</button>`));
    return form.html();
}

function getCellPosition(cell) {
    position = {
        week_id: cell.id.split(':')[0],
        day: cell.id.split(':')[1]
    }
    return position
}
