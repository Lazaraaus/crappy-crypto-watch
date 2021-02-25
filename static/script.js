// Hide Indicators Settings and submit button on page load 
$(document).ready(function() {
       // $("#rsi_settings").hide();
        $("#sma_settings").hide();
        $("#fibbonaci_settings").hide();
        $("#submit_settings").hide();
        
});

//Change indicator_settings DOM object relative to which Indicator is selected
var old_indicator = $("#indicator").val();
//var rsi_settings = $("#indicator_settings").html();
//var sma_settings = $("#sma_settings").html();
//var fibbonaci_settings = $("#fibbonaci_settings").html();

$("select").change(function () {
        // Selection is RSI
        if ($("#indicator").val() === "RSI"){
        // Store indicator as old
               // old_indicator = $("#indicator").val();
        // Check old_indicator so we know which div to fade out
                if (old_indicator === "SMA") {
                        // Fade out old settings div and fade in new one
                        $("#sma_settings").fadeOut(function() {
                                $("#rsi_settings").delay(300).fadeIn()
                        });
                old_indicator = $("#indicator").val()
                }
                if (old_indicator === "Fibbonaci") {
                        // Fade out old settings div and fade in new one
                        $("#fibbonaci_settings").fadeOut(function() {
                                $("#rsi_settings").delay(300).fadeIn()
                        });        
                old_indicator = $("#indicator").val()
                }
        }
        //Selection is SMA
        else if ($("#indicator").val() === "SMA"){
        // Store indicator as old
               // old_indicator = $("#indicator").val();
        // Check old_indicator so we know which div to fade out
                if (old_indicator === "RSI") {
                        // Fade out old settings div and fade in new one
                        $("#rsi_settings").fadeOut(function() {
                                $("#sma_settings").delay(300).fadeIn()
                        });
                old_indicator = $("#indicator").val()
                }
                if (old_indicator === "Fibbonaci") {
                        // Fade out old settings div and fade in new one
                        $("#fibbonaci_settings").fadeOut(function() {
                                $("#sma_settings").delay(300).fadeIn()
                        });
                old_indicator = $("#indicator").val()
                }
        }
        // Selection is Fibbonaci
        else if ($("#indicator").val() === "Fibbonaci"){
        // Store indicator as old
               // old_indicator = $("#indicator").val();
        // Check old indicator so we know which div to fade out
                if (old_indicator === "RSI") {
                        // Fade out old settings div and fade in new one
                        $("#rsi_settings").fadeOut(function() {
                                $("#fibbonaci_settings").delay(300).fadeIn()
                        });
                old_indicator = $("#indicator").val()
                }
                if (old_indicator === "SMA") {
                        // Fade out old settings div and fade in new one
                        $("#sma_settings").fadeOut(function() {
                                $("#fibbonaci_settings").delay(300).fadeIn()
                        });
                old_indicator = $("#indicator").val()
                }
                
        }
});


    
