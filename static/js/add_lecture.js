function renderLectureForm() {
    html = ``
}

function getCellPosition(cell) {
    position = {
        week_id: cell.id.split(':')[0],
        day: cell.id.split(':')[1]
    }
    return position
}

