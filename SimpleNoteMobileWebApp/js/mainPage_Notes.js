/*
*   Author: Sergei Papulin
*/
;
// *****************************
// NOTE PAGE
// *****************************
var pageNotes = (function() {

    var pageNotes = {},
        options = {};

    var defaults = {
        url: "http://127.0.0.1:8000/bootstrap-notes/api/v1/notes/",
        containerSelector: "#note-list-view-id",
    };

    var $container = null;

    pageNotes.init = function(params) {

        options = $.extend({}, params, defaults);
        $container = $(options.containerSelector);

        // load note list from storage
        renderNotes(pageStorage.getNoteList());
    };

    pageNotes.refresh = function() {

        // console.log("notes-page-id:refresh");

        // request notes from server
        requestData();
    };

    // =============================
    // SERVICE API
    // =============================
    function requestData() {  

        // get local timestamp
        var localTimestamp = pageStorage.getTimestamp();
        
        // request all after localTimestamp
        requestNotes(localTimestamp);
    }

    function requestNotes(timestamp) {

        var url = options.url;

        if (timestamp)
            url += "?timestamp=" + timestamp;

        $.ajax({
            type: "GET",
            url: url,
            success: onSuccessRequestNotes,
            error: onErrorRequestNotes,
            dataType: "json",
        });

        function onSuccessRequestNotes(response) {

            console.log(response);
            
            if (response.status === "OK") {

                // set local timestamp
                pageStorage.setTimestamp(response.timestamp);

                if (response.notes.length > 0) {

                    // add new notes to the storage
                    pageStorage.addNotes(response.notes);
                    
                    // render new notes
                    renderNewNotes(response.notes);
                }

            } else {
                console.log("onErrorRequestNotes => Error");
            }
        }
        function onErrorRequestNotes(e) {
            console.log(e);
            alert("Not able to reach the server");
        }
    }

    // =============================
    // STORAGE
    // =============================
    var pageStorage = {

        setTimestamp: function(value) {
            localStorage.setItem("timestamp", value);
        },
        getTimestamp: function() {
            return localStorage.getItem("timestamp");
        },
        addNotes: function(values) {
            for(var i=0; i < values.length; i++) localStorage.setItem("note_" + values[i].id, JSON.stringify(values[i]));
        },
        addNote: function(value) {
            localStorage.setItem("note_" + value.id, JSON.stringify(value));
        },
        getNote: function(key) {
            return JSON.parse(localStorage.getItem("note_" + key));
        },
        getNoteList: function() {
            var notes = [];
            for (var i = 0; i < localStorage.length; i++){
                if (localStorage.key(i).split("_")[0] == "note")
                    notes.push(JSON.parse(localStorage.getItem(localStorage.key(i))));
            }
            return notes;
        },
        removeNote: function(key) {
            localStorage.removeItem("note_" + id);
        }
    }

    // =============================
    // VIEW
    // =============================
    function renderNewNotes(notes) {
        
        html2render = '';
        for(var i=0; i < notes.length; i++) html2render += getHtmlNoteItem(notes[i]);
        $container.prepend(html2render);
        $container.listview("refresh");

    }
    function renderNotes(notes) {

        html2render = '';
        for(var i=0; i < notes.length; i++) html2render += getHtmlNoteItem(notes[i]);
        $container.html(html2render);
        $container.listview("refresh");

    } 
    function getHtmlNoteItem(note) {

        updated = note.updated.split("T");
        if (updated.length == 2) {
            date = updated[0];
            time = updated[1].split(":");
            note.updated = date + " " + time[0] + ":" + time[1];
        }
        return  '<li>' +
                    '<a href="#">' +
                        '<p>' + note.updated  + '</p>' +
                        '<h2>' + note.header + '</h2>' +
                        '<p><strong>'+ note.location + '</strong></p>' +
                        '<p>' + note.content + '</p>' +
                        '<p class="ui-li-aside"><strong>' + note.user + '</strong></p>' +
                    '</a>' +
                '</li>';
    }

    return pageNotes;

})();