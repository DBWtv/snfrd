function getEnableDays(course_id) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/class/api/enable_days/', false);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    let data = 'course_id=' + encodeURIComponent(course_id) +
        '&csrfmiddlewaretoken=' + encodeURIComponent(getCookie('csrftoken'));

    xhr.send(data);

    return JSON.parse(xhr.responseText);
}

function updateTable(day_id, course_id) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/class/api/update_table/', async = false);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    let data = 'course_id=' + encodeURIComponent(course_id) +
        '&csrfmiddlewaretoken=' + encodeURIComponent(getCookie('csrftoken')) +
        '&day_id=' + encodeURIComponent(day_id);

    xhr.send(data);

    if (xhr.status != 201) {
        throw new Error(xhr.status + ': ' + xhr.statusText);
    }

    return xhr.responseText;
}

function newCollonForm(days) {
    let html = $('<div class="form-group"></div>')
    let form = $('<form class="addColumnForm"></form>');
    let select = $('<select id="daySelected" name="day">');
    for (let i = 0; i < days.length; i++) {
        let option = $('<option>');
        option.attr('value', days[i].id);
        option.text(days[i].name);
        select.append(option);
    }
    let button = $('<button id="addColSubmit">Добавить</button>');
    form.append(select);
    form.append(button);
    html.append(form);
    return html;
}