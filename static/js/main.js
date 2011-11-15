// main

$(function() {
  $('.project').twipsy();
  $('.date-picker').datepicker({
    beforeShowDay: $.datepicker.noWeekends,
    dateFormat: $.datepicker.ISO_8601,
    minDate: new Date(),
    showOtherMonths: true,
    selectOtherMonths: true,
    numberOfMonths: 2,
    firstDay: 1
  })
});

