$(function(){
var allMap = $("#accidentMap,#constructionMap,#fogMap,#frozenMap");
        var allGraph = $("#accidentGraph,#constructionGraph,#fogGraph,#frozenGraph");
        $("#constructionGraph,#fogGraph,#frozenGraph").hide();
        $("#accidentBtn").click(function(){
          allMap.hide();
          allGraph.hide();
          $("#accidentMap").show();
          $("#accidentGraph").show();
        });
        $("#constructionBtn").click(function(){
          allMap.hide();
          allGraph.hide();
          $("#constructionMap").show();
          $("#constructionGraph").show();
        });
        $("#fogBtn").click(function(){
          allMap.hide();
          allGraph.hide();
          $("#fogMap").show();
          $("#fogGraph").show();
        });
        $("#frozenBtn").click(function(){
          allMap.hide();
          allGraph.hide();
          $("#frozenMap").show();
          $("#frozenGraph").show();
        });
      })