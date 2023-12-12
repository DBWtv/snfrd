function change_title_request(course_id, field, text) {
    xml = new XMLHttpRequest();
    xml.open("POST", "/class/api/change_about/", false);
    xml.setRequestHeader("Content-Type", "application/json");
    xml.send(JSON.stringify({
        "course_id": course_id,
        "text": text,
        "field": field
    }));

    if (xml.status == 201) {
        return xml.responseText;
    }
    else {
        alert(xml.status + ': ' + xml.responseText);
    }

}

