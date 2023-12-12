function renderEditLectureForm(position, date, title) {
    let form = $(`<form id="lecture-form:${position.week_id}:${position.day}"></form>`);
    
    // Добавляем поле для ввода даты с установленным значением
    form.append($(`<div class="form-group"><label for="lecture-date:${position.week_id}:${position.day}">Date</label>`));
    form.append($(`<input id="lecture-date:${position.week_id}:${position.day}" type="date" name="date" class="form-control" required value="${convertDateFormat(date) || ''}"></div>`));
    
    // Добавляем поле для ввода заголовка с установленным значением
    form.append($(`<div class="form-group"><label for="lecture-title:${position.week_id}:${position.day}">Title</label>`));
    form.append($(`<input id="lecture-title:${position.week_id}:${position.day}" type="text" name="title" class="form-control" required value="${title || ''}"></div>`));
    
    form.append($(`<br>`))
    // Добавляем кнопки для отправки формы и отмены редактирования
    form.append($(`<button type="submit" id="editLectureBtn">Edit</button>`));
    form.append($(`<button type="submit" id="cancelEditLectureBtn">Cancel</button>`));

    return form.html();
}


function convertDateFormat(inputDate) {
    const parts = inputDate.split('.').map(part => part.trim());
    const day = parts[0];
    const month = parts[1];
    const year = parts[2];

    return `${year}-${month}-${day}`;
}