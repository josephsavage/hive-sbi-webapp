$(function () {
  'use strict';
  
  $(".delivered_votes_modal_link").on("click", function() {
    console.log("HOLA")
    let post_title = $(this).closest("tr").data("title")
    $("#deliveredVotesModalLabel").text(post_title)
  })
})
