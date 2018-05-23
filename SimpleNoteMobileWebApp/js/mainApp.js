/*
    Author: Sergei Papulin
*/
;
(function() {
    $(document).ready(function() {

        // INITIALIZATION
        pageNotes.init();
        pageNotes.refresh();

        pageMyNotes.init();
        pageCreateNote.init();
        pageAccount.init();

        $("#btn-id").click( function() {
            $.mobile.changePage("#notes-page-id", {transition: "flip", reverse: false});
        });

        // EVENTS
        // Footer Button Event
        $(".notes-page-btn-id").click(function() {
            $.mobile.changePage("#notes-page-id", {transition: "flip", reverse: false});
        });
        $(".my-notes-page-btn-id").click(function() {
            $.mobile.changePage("#my-notes-page-id", {transition: "flip", reverse: false});
        });
        $(".create-note-page-btn-id").click(function() {
            $.mobile.changePage("#create-note-page-id", {transition: "flip", reverse: false});
        });
        $(".account-page-btn-id").click(function() {
            $.mobile.changePage("#account-page-id", {transition: "flip", reverse: false});
        });

        $("#notes-page-id").on( "pagebeforeload", function( event, ui ) {
            console.log("pagebeforeload");
            pageNotes.refresh();
        });

        // Header Button Event
        $(".refresh-btn-id").click(function() {
            pageNotes.refresh();
        });

        // Before Show
        $("#notes-page-id").on( "pagebeforeshow", function( event, ui ) {
            console.log("pagebeforeshow");
            pageNotes.refresh();
        });
        $("#my-notes-page-id").on( "pagebeforeshow", function( event, ui ) {
            pageMyNotes.refresh();
        });
        $("#create-note-page-id").on( "pagebeforeshow", function( event, ui ) {
            pageCreateNote.refresh();
        });
        $("#account-page-id").on( "pagebeforeshow", function( event, ui ) {
            pageCreateNote.refresh();
        });
    });
})();