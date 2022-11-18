$(function () {
  'use strict';
  
  $(".delivered_votes_modal_link").on("click", function() {
    let post_title = $(this).closest("tr").data("title")

    $("#deliveredVotesModalLabel").text(post_title)
    $("#idPostVotesTBody").html("")

    let post_votes = ($(this).closest("tr").data("post-votes"))
    let post_votes_tbody_html = ""

    post_votes.forEach(function (vote, index) {
      let vote_tr = "<tr><td>" + vote.voter + "</td><td>" + vote.hive_power_rewards + "</td><td>" + vote.hbd_rewards + "</td></tr>"
      post_votes_tbody_html = post_votes_tbody_html + vote_tr

      $("#idPostVotesTBody").html(post_votes_tbody_html)
    });
  })
})
