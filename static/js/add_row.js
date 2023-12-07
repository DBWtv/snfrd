function addRowRequest(week_id) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/class/api/add_row/", false);  // Устанавливаем параметр false для синхронного режима
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

    // Формируем тело запроса
    var data = 'week_id=' + encodeURIComponent(week_id) +
            '&course_id=' + encodeURIComponent('{{ course.id }}') +
            '&csrfmiddlewaretoken=' + encodeURIComponent('{{ csrf_token }}');

    xhr.send(data);

    if (xhr.status === 201) {
        return true;
    } else {
        throw new Error(xhr.status + ': ' + xhr.statusText);
    }
}

function addRow(weekCell, numCols, table) {
    // Создаем новую строку
    var newRow = $('<tr>');

    var cellHTML = $('#emptyCell').html();

    // Добавляем ячейки с данными
    for (var i = 1; i < numCols; i++) {
        if (i != 1) {
            newRow.append('<td>' + cellHTML + '</td>');
        } else {
            newRow.append('<td class="calendarWeekCell">' + weekCell + '</td>');
        }
    }

    // Добавляем новую строку в конец таблицы
    table.append(newRow);

    // Копируем содержимое последней строки
    var lastRowContent = $('#lastRow').html();

    // Удаляем существующую кнопку
    $('#lastRow').remove();

    // Добавляем новую строку с содержимым последней строки
    table.append('<tr id="lastRow">' + lastRowContent + '</tr>');
}

$(document).ready(function () {
    // Обработчик события нажатия кнопки
    $('#schedule').on('click', '#addRow', function () {

        // Выбираем таблицу и определяем количество столбцов
        var table = $('#schedule tbody');
        var numCols = $('#schedule thead th').length;

        var weekCell = $('#schedule tbody .calendarWeekCell').length + 1;

        try {
            addRowRequest(weekCell)
            addRow(weekCell, numCols, table);
        }
        catch (e) {
            console.log(e);
        }

    });
});