function addRowRequest(week_id, course_id) {
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/class/api/add_row/", false);  // Устанавливаем параметр false для синхронного режима
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Формируем тело запроса
    let data = 'week_id=' + encodeURIComponent(week_id) +
            '&course_id=' + encodeURIComponent(course_id) +
            '&csrfmiddlewaretoken=' + encodeURIComponent(getCookie('csrftoken'));

    xhr.send(data);

    if (xhr.status === 201) {
        return true;
    } else {
        throw new Error(xhr.status + ': ' + xhr.statusText);
    }
}

function addRow(weekCell, numCols, table) {
    // Создаем новую строку
    let newRow = $('<tr>');

    let cellHTML = `
        <button class="btn" id="addCell">
            <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 20 20">
                <path fill="#888888" d="M10 1.6a8.4 8.4 0 1 0 0 16.8a8.4 8.4 0 0 0 0-16.8zm5 9.4h-4v4H9v-4H5V9h4V5h2v4h4v2z"></path>
            </svg>
        </button>`

    // Добавляем ячейки с данными
    for (var i = 1; i < numCols; i++) {
        if (i != 1) {
            newRow.append('<td id="emptyCell">' + cellHTML + '</td>');
        } else {
            newRow.append('<td class="calendarWeekCell">' + weekCell + '</td>');
        }
    }

    // Добавляем новую строку в конец таблицы
    table.append(newRow);

    // Копируем содержимое последней строки
    let lastRowContent = $('#lastRow').html();

    // Удаляем существующую кнопку
    $('#lastRow').remove();

    // Добавляем новую строку с содержимым последней строки
    table.append('<tr id="lastRow">' + lastRowContent + '</tr>');
}
