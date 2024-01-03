function renderEditLectureForm(position, date, title) {
    let form = $(`<form id="lecture-form:${position.week_id}:${position.day}:${position.lecture_id}"></form>`);
    
    // Добавляем поле для ввода даты с установленным значением
    form.append($(`<div class="form-group"><label for="lecture-date:${position.week_id}:${position.day}">Дата</label>`));
    form.append($(`<input id="lecture-date:${position.week_id}:${position.day}" type="date" name="date" class="form-control" required value="${convertDateFormat(date) || ''}"></div>`));
    
    // Добавляем поле для ввода заголовка с установленным значением
    form.append($(`<div class="form-group"><label for="lecture-title:${position.week_id}:${position.day}">Название</label>`));
    form.append($(`<input id="lecture-title:${position.week_id}:${position.day}" type="text" name="title" class="form-control" required value="${title || ''}"></div>`));
    
    form.append($(`<br>`))
    // Добавляем кнопки для отправки формы и отмены редактирования
    s_button = $(`<button type="submit" id="submitEditLectureBtn">Сохранить</button>`);
    c_button = $(`<button type="button" id="cancelEditLectureBtn">Отмена</button>`);
    
    form.append(s_button);
    form.append(c_button);

    return form.html();
}


function convertDateFormat(inputDate) {
    const parts = inputDate.split('.').map(part => part.trim());
    const day = parts[0];
    const month = parts[1];
    const year = parts[2];

    return `${year}-${month}-${day}`;
}
